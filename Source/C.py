import tkinter as tk 
from tkinter import *
import time
from datetime import date,datetime
import pyautogui
import threading 
import os

from pynput.keyboard import Key, Listener

from thong_bao_thoi_gian import *

#Lưu biến để lưu thư mục chứa ảnh chụp màn hình là ngày - tháng
name_dir_now = datetime.now().strftime("%d-%m")

#Biến lưu để chương trình đẵ stop hay chưa (để giải quyết phần lưu các phím đã bấm)
stop = {'stop': False}

#Biếu lưu để biết chưa trình có đang mới bắt đầu, nếu bắt đầu xong thì đổi sang False (để lưu giờ bắt đầu của lịch sử)
start = {'start': True}

#Biến lưu Duration đến ngược
Duration = {'D': None}

#Biến lưu Interrupt là thời gian chương trình hết nghỉ (có thể sử dụng máy khi time hiện tại bằng thời gian đã lưu trong Interrupt)
Interrupt = {'I': None}

#Biến lưu Tổng thời gian cho phép sử dụng đếm ngược (lưu băng giây)
Sum = {'S': None}

Path = {"P": os.path.dirname(os.path.abspath(__file__))}

def Child():

    #Khởi tạo
    app_window = tk.Tk()
    app_window.title("Child") 
    app_window.geometry("470x350+400+200") 
    app_window.config(bg="#f2e750")
    app_window.resizable(0,0)
    Label(app_window,text="THỜI GIAN CÒN LẠI", font=("Times New Roman",15),padx = 10,pady = 10,bg="#f2e750", fg="#363529").pack()
    label = Label(app_window, font=("Boulder", 68, 'bold'),bg="#f2e750", fg="#363529", bd=25)
    label.pack()

    #Đọc Tổng thời gian được phép sử dụng từ file (biến trả về dưới dạng giây) trong file khung giờ hoặc file đã lưu Sum trước đó
    Sum['S'] = computeSum(datetime.today().time(), use_time_datas(Path['P'] + '/text.txt'))
    
    #Đọc Duration từ file khung giờ
    Duration['D'] = readDuration(datetime.today().time(), use_time_datas(Path['P'] + '/text.txt')) #Read từ file khung giờ ra Duration trong khoảng thời gian đó

    #Nếu Duration tồn tại, thì chuyển Duration sang dạng second để đếm ngược
    if Duration['D'] != None:
        Duration['D'] = int(Duration['D'])*60

    #Xử lý khung thời gian và đồng hồ đếm ngược
    digital_clock(app_window,label)

    #Ghi lại các phím đã bấm
    try:
        t2 = threading.Thread(target=key_press, args=tuple())
        t2.start()

    except Exception as e:
        print (e)

    app_window.mainloop()

    #Nếu chương trình kết thúc
    if str(app_window) == '.':
        stop['stop'] = True

        #Lưu thời gian kết thúc trong phần lịch sử
        today = date.today().strftime("%d-%m")
        with open(Path['P'] + '\\history_time\\' + today + '.txt',mode='a') as f:
           f.write(str(time.strftime("%H:%M")) + '\n')

        #Lưu lại thời gian đếm ngược của Sum để sử dụng cho lần sử dụng tới trong khung thời gian này KHI tồn tại Sum
        if Sum['S'] != None:
            save_sum(Sum['S'],use_time_datas(Path['P'] + '/text.txt'))

#Hàm đếm ngược và giải quết các vấn đề về thời gian
def digital_clock(app_window, label): 

   #Đọc danh sách khung giờ được sử dụng
   data = readFileText()
   
   #Nếu đây là lần chạy vòng lặp đầu (mới bắt đầu chương trình)
   if start['start'] == True:

       #Lưu thời gian bắt đầu trong phần lịch sử
       today = date.today().strftime("%d-%m")
       with open(Path['P'] + '\\history_time\\' + today + '.txt',mode='a') as f:
           f.write(str(time.strftime("%H:%M")) + '~')
       start['start'] = False

   #Biến t1 lưu thời gian hiện thời 
   t1 = datetime.today()

   #Biến t2 lưu thời gian kết thúc (thời gian kết thúc được tính theo SUM hoặc TO)
   t2 = None
   
   for data1 in data:
       #Nếu thời gian hiện tại nằm trong thời gian khung thời gian cho phép sử dụng
       if datetime.strptime(data1['F'] + ':00','%H:%M:%S').time() <= t1.time() and t1.time() < datetime.strptime(data1['T'] + ':00','%H:%M:%S').time():

           #Nếu không tồn tại SUM thì tính t2 bằng TO (thời gian kết thúc được lưu lại trong khung giò) 
           if Sum['S'] == None:
               t2 = datetime.strptime(str(datetime.today()).split(' ')[0] +'-'+ data1['T'] + ':00','%Y-%m-%d-%H:%M:%S')

           #Nếu tồn tại SUM
           else:
               #Nếu không tồn tại Interrupt và Duration (Interrupt và Duration cùng tồn tại hoặc cùng không tồn tại)
               if data1['I'] == None:

                   #Nếu thời gian hiện tại + SUM lớp hơn thời gian TO thì t2 được tính là TO (lấy thời gian kết thúc nhỏ hơn)
                   if (t1 + timedelta(seconds=Sum['S'])) >= datetime.strptime(str(datetime.today()).split(' ')[0] +'-'+ data1['T'] + ':00','%Y-%m-%d-%H:%M:%S'):
                       t2 = datetime.strptime(str(datetime.today()).split(' ')[0] +'-'+ data1['T'] + ':00','%Y-%m-%d-%H:%M:%S')

                   #Nếu thời gian hiện tại + SUM nhỏ hơn thời gian TO thì t2 được tính là timenow + SUM 
                   else:
                       t2 = (t1 + timedelta(seconds=Sum['S']))

               #Nếu tồn tại Interrupt và Duration
               else:
                   #thời gian TO được lưu dưới dạng datetime (với ngày là hôm nay)
                   to_time_temp = datetime.strptime(str(datetime.today()).split(' ')[0] +'-'+ data1['T'] + ':00','%Y-%m-%d-%H:%M:%S')

                   #Tính số lần Interrupt trong khoảng thời gian SUM
                   index = Sum['S']/60/int(data1['D'])
                   if index == int(index):
                      index -= 1
                   index = int(index)

                   #Nếu thời gian hiện tại + SUM + thời gian Interrupt lớn hơn thời gian TO thì t2 được tính bằng TO
                   if (t1 + timedelta(seconds=Sum['S'] + index*int(data1['I'])*60)) >= to_time_temp:
                       t2 = datetime.strptime(str(datetime.today()).split(' ')[0] +'-'+ data1['T'] + ':00', '%Y-%m-%d-%H:%M:%S')

                   #Nếu ngược lại thì t2 được tính bằng thời gian hiện tại + SUM (do trong khoảng thời gian Interrupt SUM không thay đổi)
                   else:
                       temp = (t1 + timedelta(seconds=Sum['S'])).time()
                       t2 = (t1 + timedelta(seconds=Sum['S']))   
           break

   #Nếu thời gian hiện tại không nằm trong khung thời gian cho phép sử dụng
   if t2 == None:
       app_window.quit()
       app_window.destroy()
       return
   
   #Nếu Duration tồn tại
   if Duration['D'] != None:

       #Nếu Duration = 0 tức là chương trình đã chạy đủ 1 khoảng thời gian Duration
       if Duration['D'] == 0:
           #Lưu Interrupt vào file (phòng trường hợp trong khoảng Interrupt trẻ tắt máy và bật lại)
           initializeInterrupt(datetime.today().time(), use_time_datas(Path['P'] + '/text.txt'))
           Interrupt['I'] = datetime.strptime(readInterrupt(Path['P'] + '/data/history/interrupt.txt').split(' ')[1],'%H:%M:%S').time()

           #sleep system
           os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

       if Interrupt['I'] != None:
           #Nếu Interrupt lớn hơn thời gian hiện tại, tức là vẫn nằm trong thời gian Interrupt
           if Interrupt['I'] > datetime.today().time():

               #sleep system nếu như trẻ có ý định bật lại máy
               try:
                   os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
               except:
                   err = None
           #Nếu ngược lại, tức là khoảng thời gian Inrerrupt đã hết trẻ có thể bật lại máy
           else:
               #Khởi tạo lại biến đếm ngược Duration
               Duration['D'] = int(readDuration(datetime.today().time(), use_time_datas(Path['P'] + '/text.txt')))*60

               #Xóa dữ liệu Interrupt đã lưu trước đó
               with open(Path['P'] + '/data/history/interrupt.txt','w') as f:
                   f.write('')
               Interrupt['I'] = None

   #Thời gian đếm ngược
   time_count = datetime.strptime(str(t2-t1).split('.')[0],'%H:%M:%S')

   #Nếu thời gian đếm ngược nhỏ hơn 1 phút
   if time_count.time() <= datetime.strptime("0:01:00",'%H:%M:%S').time():

       #Xuất ra thời gian tiếp theo có thể sử dụng
       Label(app_window,text="CÓ THỂ BẬT MÁY LẦN TỚI VÀO LÚC:", font=("Times New Roman",15),padx = 10,pady = 10,bg="#f2e750", fg="#363529").place(x=10, y=200)
       Label(app_window,text=str(next_use_time(datetime.today().time(),use_time_datas(Path['P'] + '/text.txt'))), font=("Times New Roman",15),padx = 10,pady = 10,bg="#f2e750", fg="#363529").place(x=180, y=250)
   
   #Nếu thời gian đếm ngược kết thúc, tắt
   if time_count.time() < datetime.strptime("0:00:01",'%H:%M:%S').time() :
       app_window.quit()
       app_window.destroy()
       return

   if str(label['text']) != '':

       #Nếu như label thay đổi sô phút (tức 1p trôi qua)
       if str(label['text']).split(':')[1] != str(time_count.time()).split(':')[1]:
           #Chụp màn hình
           screenshot()

   #Đếm ngược SUM
   if Sum['S'] != None:
        Sum['S'] -= 1

   #In thời gian đếm ngược
   label.config(text=str(time_count.time()))

   #Đếm ngược Duration
   if Duration['D'] != None:
        Duration['D'] -= 1

   #1s sau tiếp tục xét hàm digital_clock 
   label.after(1000, lambda:  digital_clock(app_window, label))

#Hàm đọc khung giờ file test, hàm trả trả về 1 list các khung giờ
def readFileText():
    f = open(Path['P'] + "\\text.txt", 'r')
    data = f.read().split('\n')
    data_list = []
    for data1 in data:
        if data1 == '':
            continue
        data_dict = {'F': None,'T': None, 'D': None, 'I': None, 'S': None}
        data2 = data1.split(' ')
        for i in data2:
            if i[0] == 'F':
                data_dict['F'] = i.replace('F','')
            if i[0] == 'T':
                data_dict['T'] = i.replace('T','')
            if i[0] == 'D':
                data_dict['D'] = i.replace('D','')
            if i[0] == 'I':
                data_dict['I'] = i.replace('I','')
            if i[0] == 'S':
                data_dict['S'] = i.replace('S','')
        data_list.append(data_dict)
    return data_list

#Hàm chụp ảnh màn hình và lưu lại
def screenshot():
    # Ten thu muc image trong o dia google drive.
    image_path = Path['P'] + '\\image'

    image_today_path = f'{image_path}\\{name_dir_now}'

    # Check xem thu muc da ton tai hay chua
    is_dir = os.path.isdir(image_today_path)
    # Neu chua thi tao thu muc
    if is_dir == False:
        os.mkdir(image_today_path)
    id_screenshot = datetime.now().strftime("%H-%M")

    id_screenshot = datetime.now().strftime("%H-%M")
    # Chup screenshot
    try:
        screenshot = pyautogui.screenshot()
        # Lay id_screenshot la thoi diem gio:phut hien tai
        screenshot.save(f'{image_today_path}\\{id_screenshot}.png')
    except:
        err = None

#Hàm lấy các phím đã bấm
def key_press():
    with Listener( 
        on_press=press) as listener:
        listener.join()

#Hàm lấy phím và lưu lại
def press(key):
    if stop['stop'] == True:
        return False
    # Ten thu muc image trong o dia google drive.
    key_path = Path['P'] + '\\key'

    key_today_path = f'{key_path}\\{name_dir_now}'

    with open(f'{key_today_path}.txt', mode='a') as f:
        f.write(str(key).replace("'","") + '\n') 
