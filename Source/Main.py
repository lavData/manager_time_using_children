from tkinter import * 
from PIL import Image, ImageTk

import time
from datetime import datetime, date
import threading

from thong_bao_thoi_gian import * 
from C import Child, readFileText

from gtts import gTTS
from playsound import playsound
import os

'''
Sử dụng thư viện: tkinter,PIL, time, datetime, threading, gtts, playsound, os, pyautogui, pynput, glob
'''

# Biến kiểm tra xem khi đăng nhập, user có phải là Child hay không, mắc định là False
is_child = {"is_child": False}

# Biến kiểm tra xem khi đăng nhập, user có phải là Parent hay không, mắc định là False
is_parent = {"is_parent": False}

# Biến đếm xem số lần sau mật khẩu khi nhập, mắc định là 1
index_false_password = {"f": 1}

#Biến đếm xem số lần bấm vào nút đăng nhập (Xử lý phần không nằm trong thời gian được dùng)
index_login = {"i" : 0,"i1" : 0}

#Biến lưu Path hiện tại của thư mục
Path = {"P": os.path.dirname(os.path.abspath(__file__)) + '/'}

class Login(Frame):
    #Khởi tạo
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.initUI()

    #Khởi tạo UI
    def initUI(self): 
        self.pack(fill=BOTH, expand=YES)

        #background
        self.image = Image.open(Path['P'] +"background.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        #Title
        self.Title = Label(text="GIÁM SÁT SỬ DỤNG MÁY TÍNH",background="#17EFF4") 
        self.Title.config(font=("Times New Roman",20)) 
        self.Title.place(bordermode=OUTSIDE, height=50, x= 150,y=80) 

        #Password label
        self.pw = Label(text="Password")                                                    
        self.pw.config(font=("Times New Roman",15)) 
        self.pw.place(bordermode=OUTSIDE, height=50, x= 250,y=250) 


        #Password entry
        self.pw_text = StringVar()
        self.pw_entry = Entry(textvariable=self.pw_text,show='*') 
        self.pw_entry.config(font=("Times New Roman",15))
        self.pw_entry.place(bordermode=OUTSIDE, height=50, width=310, x= 450,y=250)


        #Login button
        self.login_button = Button(self, text="Đăng nhập", background="#13857D",command = self.signIn)
        self.login_button.config(font=("Times New Roman",15))
        self.login_button.place(bordermode=OUTSIDE,height=40,x=530, y=370)

        #Biến lưu label hiển thị thông báo giờ có thể sử dụng khi thời gian hiện tại không hợp với khung giờ
        self.label = Label()

        #Biến lưu label hiển thị khi đăng nhập sai
        self.false_signal1 = Label()

        #Biến lưu id của label.after để có thể tắt sự kiện lặp
        self.after_id = None

        #Biến lưu thread của sound thông báo giờ truy cập tiếp theo
        self.t2 = None

        self.mainloop()
        self.quit()

    #Hàm resize background khi phóng to hay thu nhở cửa sổ 
    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)      
        self.background.configure(image =  self.background_image)

    #Hàm đăng nhập khi bấm vào nút đăng nhập
    def signIn(self):
        self.false_signal1.destroy()

        #Đọc thông tin mật khẩu đẵ nhập
        f = open(Path['P'] +"data/user.dat","rb")
        data = f.read().decode()
        data_list = data.split('\n')

        #Nếu mật khẩu nhập vào là mật khẩu của Parent
        if 'p' + self.pw_text.get() in data_list:
            index_login['i1'] = 0
            self.pw_entry.delete(0,END)

            try:
                #Xóa sự kiện 15s sau NẾU nhập mật khẩu lần đầu không phải parent và không nằm trong khung giờ Child
                self.label.after_cancel(self.after_id)                
                #Xóa thread đang thông báo giờ kết thúc NẾU lần nhập đầu tiên không phải là parent và không nằm trong khung giờ Child
                self.stop_event.set()
            except:
                self.label = None

            #Thiết lập cho biến để biết người nhập vào là Parent
            is_parent["is_parent"] = True
            self.quit()
            return

        #Đọc dữ liệu về khung giờ Child
        data = readFileText()
        t1 = datetime.strptime(time.strftime("%H:%M:%S"),'%H:%M:%S')

        #Kiểm tra xem có đang là trong khung giờ có thể sử dụng
        can_use = False
        for data1 in data:
            if datetime.strptime(data1['F'] + ':00','%H:%M:%S') <= t1 and t1 < datetime.strptime(data1['T'] + ':00','%H:%M:%S'):
                can_use = True
                break

        #Nếu không nằm trong khung giờ sử dụng
        if can_use == False:

            #Nếu không phải là bấm nút sai lần đầu thì trả về mà không thực hiện báo giờ tiếp theo được dùng
            if index_login['i1'] != 0:
                return

            #Nếu là lần đầu bấm nút sai thì thông báo về giờ được sử dụng và đặt hạn 15s sau sẽ kết thúc
            index_login['i1'] += 1
            time_next = str(next_use_time(datetime.today().time(),use_time_datas(Path['P'] + 'text.txt')))
            self.script = time_next + " mới được sử dụng"
            try:
                self.t2 = threading.Thread(target=self.Notification, args=tuple())
                self.stop_event = threading.Event()
                self.t2.start()
            except Exception as e:
                print (e)
            self.label = Label(self,text=self.script,font=("Times New Roman",15),fg="#D03838")
            self.label.place(bordermode=OUTSIDE,height=40,x=490, y=430)
            self.after_id = self.label.after(15*1000, lambda: self.quit())
            return

        #Nếu mật khẩu nhập vào là Child
        if 'c' + self.pw_text.get() in data_list:
            is_child["is_child"] = True
            self.quit()

        #Nếu mật khẩu nhập không đúng
        else:
            #Hiển thị thông báo "Sai mật khẩu"
            self.pw_entry.delete(0,END)
            self.false_signal1 = Label(text="Sai mật khẩu")
            self.false_signal1.config(font=("Times New Roman",10),fg="#D03838")
            self.false_signal1.place(bordermode=OUTSIDE,x=550, y=300)

            #Nếu số lần sai mật khẩu là 3
            if index_false_password['f'] >= 3:

                #Lưu lại thời gian 10p sau mời đăng nhập
                with open(Path['P'] +'data/status.txt','w') as f1:
                    today = time.strftime("%H:%M")
                    m = int(str(today).split(':')[1]) + 10
                    h = int(str(today).split(':')[0])
                    if m >= 60:
                        m -= 60
                        h += 1
                        if h>=24:
                            h = 0
                    today = date.today().strftime("%d-%m") 
                    f1.write(str(today) + ' ' + str(h) + ':' + str(m))
                self.quit()
                return

            index_false_password['f'] += 1

    #Hàm thông báo dạng âm thanh giờ tiếp theo sử dụng
    def Notification(self):
        tts = gTTS(text=self.script, lang="vi")
        tts.save(Path['P'] +'alert' + str(index_login['i']) +'.mp3')
        playsound(Path['P'] +'alert' + str(index_login['i']) +'.mp3')
        os.remove(Path['P'] +'alert'+str(index_login['i']) +'.mp3')
        index_login['i'] +=1

#--------------------------------------MAIN-----------------------------------------------
if __name__ == '__main__':
    while True:
        #Kiểm tra xem có đang là thời gian cấm đăng nhập do nhập sai mật khẩu lần thứ 3
        with open(Path['P'] + 'data/status.txt','r') as f:
            data = f.read()
            if data != '':
                if datetime.strptime(time.strftime("%H:%M"),'%H:%M').time() >= datetime.strptime(data.split(' ')[1],'%H:%M').time() or data.split(' ')[0] != str(date.today().strftime("%d-%m")):
                    with open(Path['P'] +'data/status.txt','w') as f1: 
                        f1.write('')
                else:
                    break

        #Kiêm tra xem có đang là thời gian nghỉ của khung giờ hay không (trường hợp trẻ trong khoảng Interrupt thì tắt máy và bật lại)
        with open(Path['P'] +'data/history/interrupt.txt','r') as f:
            data = f.read()
            if data != '':
                try:
                    a = data.split(' ')[1]
                    b = datetime.strptime(a,'%H:%M:%S').time()
                    if datetime.today().time() >= b or data.split(' ')[0] != str(date.today().strftime("%d:%m")):
                        with open(Path['P'] +'data/history/interrupt.txt','w') as f1: 
                            f1.write('')
                    else:
                        break
                except:
                    err = None

        #Khởi chạy app
        L = Tk()
        L.title("Đăng nhập")
        L.geometry("900x600+100+100")
        main_after_id = L.after(60*1000, L.quit)
        app = Login(L)
        try:
            L.destroy()
        except:
            err = None

        #Nếu là mật khẩu phụ huynh
        if is_parent['is_parent'] == True:

            #Thiết lập thời gian hỏi lại mật khẩu (chạp lại app đăng nhập)
            L.after_cancel(main_after_id)
            time.sleep(60)
            is_parent['is_parent'] = False
            index_false_password['f'] = 1
            continue

        #Nếu là mật khẩu Child
        if is_child['is_child'] == True:
            L.after_cancel(main_after_id)
            Child()
        break

    os.system("shutdown /s /t 1")
