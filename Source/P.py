import tkinter as tk
from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import date
import glob
import time
import threading


def Parent():
    #Khởi tạo
    p = tk.Tk()
    p.title("Parent")
    p.geometry("1000x650+100+100")

    #Khởi tạo 4 tab hiển thị các data các chức năng
    tabControl = ttk.Notebook(p)
    tabKhungGio = ttk.Frame(tabControl,height=4000,width=4000)
    tabLichSu = ttk.Frame(tabControl,height=4000,width=4000)
    tabHinhAnh = ttk.Frame(tabControl,height=4000,width=4000)
    tabKey = ttk.Frame(tabControl,height=4000,width=4000)

    tabKhungGio.pack(fill=BOTH, expand=True)
    tabLichSu.pack(fill=BOTH, expand=True)
    tabHinhAnh.pack(fill=BOTH, expand=True)
    tabKey.pack(fill=BOTH, expand=True)

    tabControl.add(tabKhungGio, text='KHUNG GIỜ SỬ DỤNG')
    tabControl.add(tabLichSu, text='LỊCH SỬ SỬ DỤNG')
    tabControl.add(tabHinhAnh, text='LỊCH SỬ HÌNH ẢNH')
    tabControl.add(tabKey, text='LỊCH SỬ KEY')
    tabControl.pack(expand=True, fill=BOTH,pady=10)

    #---------------------TabKhungGio-----------------------
    #Đọc các thông tin khung giờ sử dụng
    data = readFileText()

    #Write Title
    frame_KhungGio2 = Frame(tabKhungGio)
    frame_KhungGio2.pack(side=BOTTOM)

    label_khungGio = Label(tabKhungGio,text="KHUNG GIỜ SỬ DỤNG", font=("Times New Roman",15),padx = 10,pady = 10)
    label_khungGio.pack()
    scrollbar_KhungGio = Scrollbar(tabKhungGio)
    text_KhungGio = Text(tabKhungGio,font=("Times New Roman",15),width=70,height=300, wrap = NONE,yscrollcommand = scrollbar_KhungGio.set)

    #Write button, các button có chức năng đổi mật khẩu USER và điều chỉnh khung giờ
    Button(frame_KhungGio2, text="ĐIỀU CHỈNH",font=("Times New Roman",15),command=lambda: DieuChinh(text_KhungGio, data, 's'),width=15, background="#C4C4C4").pack(side=RIGHT,fill=NONE,pady=10,padx=20)
    Button(frame_KhungGio2, text="ĐỔI MẬT KHẨU",font=("Times New Roman",15),command=lambda: ChangePassword(),width=15, background="#C4C4C4").pack(side=LEFT,fill=NONE,pady=10,padx=20)
    Button(frame_KhungGio2, text="THÊM",font=("Times New Roman",15),command=lambda: DieuChinh(text_KhungGio, data, 't'),width=15, background="#C4C4C4").pack(side=RIGHT,fill=NONE,pady=10,padx=20)
    Button(frame_KhungGio2, text="XÓA",font=("Times New Roman",15),command=lambda: DieuChinh(text_KhungGio, data, 'x'),width=15, background="#C4C4C4").pack(side=RIGHT,fill=NONE,pady=10,padx=20)
    scrollbar_KhungGio.pack(side = RIGHT, fill = Y)

    #Viết data khung giờ để hiển thị
    text_KhungGio.insert(END,"FROM\tTO\tDURATION\t\tINTERRUPT TIME\t\t\tSUM\n\n")
    for i in range(len(data)):
        text_KhungGio.insert(END, data[i]['F'] + '\t' + data[i]['T'] + '\t' + str(data[i]['D']) + '\t\t' + str(data[i]['I']) + '\t\t\t' + str(data[i]['S']) + '\n\n')

    text_KhungGio.pack(fill=Y)
    scrollbar_KhungGio.config(command=text_KhungGio.yview)
    text_KhungGio['state'] = 'disabled'

    #Update thông tin khung giò sau 1s (cập nhập dữ liệu parent khác sửa)
    update(text_KhungGio, label_khungGio)
    today = str(date.today().strftime("%d-%m"))

    #----------------------TabLichSu--------------------------
    frame_LishSu2 = Frame(tabLichSu)
    frame_LishSu2.pack(side=TOP)

    #Write tilte
    Label(frame_LishSu2,text="LỊCH SỬ SỬ DỤNG MÁY", font=("Times New Roman",15),padx = 70,pady = 10).pack(side=LEFT)

    #entry nhập vào ngày muốn xem lịch sử và button 'chọn' 
    Label(frame_LishSu2,text="Ngày", font=("Times New Roman",15),padx = 10,pady = 10).pack(side=LEFT)
    entry_ls = Entry(frame_LishSu2,exportselection=1,font=("Times New Roman",15),width=5)
    entry_ls.pack(side=LEFT)

    scrollbar_LichSu = Scrollbar(tabLichSu)
    text_LichSu = Text(tabLichSu,font=("Times New Roman",15),width=70,height=300, wrap = NONE,yscrollcommand = scrollbar_LichSu.set)

    Button(frame_LishSu2, text="Chọn",font=("Times New Roman",15),command=lambda: XemLichSuNgayKhac(tabLichSu,text_LichSu, entry_ls.get()),width=5, background="#C4C4C4").pack(side=RIGHT,padx=10)

    #Đọc file lịch sử ngày hiện tại
    data_ls = []
    try:
        f = open(".\\history_time\\" + today + ".txt", 'r')
        data_ls = f.read().split('\n')
    except:
        data_ls = []
    scrollbar_LichSu.pack(side = RIGHT, fill = Y)

    #Ghi dữ liệu lịch sử ngày hiện tại để hiển thị
    text_LichSu.insert(END,"\t\tFROM\t\t\t\tTO\n\n")
    for i in range(len(data_ls)):
        if data_ls[i] != '':
            text_LichSu.insert(END, '\t\t' + data_ls[i].split('~')[0] + '\t\t\t\t' + data_ls[i].split('~')[1] + '\n\n')

    text_LichSu.pack(fill=Y)
    scrollbar_LichSu.config(command=text_LichSu.yview)
    text_LichSu['state'] = 'disabled'

    #-------------------TabHinhAnh------------------------
    frame_HinhAnh2 = Frame(tabHinhAnh)
    frame_HinhAnh2.pack(side=BOTTOM)

    frame_HinhAnh1 = Frame(tabHinhAnh,height=20)
    frame_HinhAnh1.pack(side=TOP)

    frame_HinhAnh3 = Frame(tabHinhAnh)
    frame_HinhAnh3.pack(side=TOP)

    #Write title
    Label(frame_HinhAnh1,text="LỊCH SỬ HÌNH ẢNH", font=("Times New Roman",15),padx = 10,pady = 10).pack(side = LEFT,padx=90)

    #entry nhập vào ngày muốn xem lịch sử
    Label(frame_HinhAnh1,text="Ngày", font=("Times New Roman",15),padx = 10,pady = 10).pack(side = LEFT,padx = 10)
    entry_ha = Entry(frame_HinhAnh1,font=("Times New Roman",15),width=5)
    entry_ha.pack(side = LEFT,padx=10)

    H = {'images': [], 'index_images': 0, 'image_label': []}

    #button để xem hình ảnh trước đó
    Button(frame_HinhAnh2, text="<",font=("Times New Roman",15),width=2, command=lambda: HinhAnhTruoc(frame_HinhAnh3,H),background="#C4C4C4").pack(side=LEFT,padx = 40,pady=10)
    #button để xem hình ảnh kế tiếp
    Button(frame_HinhAnh2, text=">",font=("Times New Roman",15),width=2, command=lambda: HinhAnhKeTiep(frame_HinhAnh3,H),background="#C4C4C4").pack(side=LEFT,padx = 40,pady=10)
    #button để xem tập hình ảnh ngày đã nhập
    Button(frame_HinhAnh1, text="Chọn",font=("Times New Roman",15),command=lambda: XemHinhAnhNgayKhac(frame_HinhAnh3,H, entry_ha.get()),width=5, background="#C4C4C4").pack(side = RIGHT,padx=10)

    #Đọc hình ảnh ngày hôm nay
    for file in glob.glob(".\\image\\"+ today +"\\*"):
        try:
            image = Image.open(file)
        except:
            continue
        resize_image = image.resize((879,500))
        Image2 = ImageTk.PhotoImage(resize_image)
        H['images'].append(Image2)

    #Ghi hình ra để hiển thị
    if len(H['images']) != 0:

        for i in range(len(H['images'])):
            H['image_label'].append(None)

        H['image_label'][H['index_images']] = Label(frame_HinhAnh3, image=H['images'][H['index_images']])
        H['image_label'][H['index_images']].pack(side=LEFT,pady=20)    

    #----------------------TabKey---------------------------
    frame_Key = Frame(tabKey)
    frame_Key.pack(side=TOP)

    #Write title
    Label(frame_Key,text="LỊCH SỬ PHÍM", font=("Times New Roman",15),padx = 80,pady = 10).pack(side=LEFT)
    Label(frame_Key,text="Ngày", font=("Times New Roman",15),padx = 10,pady = 10).pack(side=LEFT)

    #entry nhập ngày muốn xem key
    entry_k = Entry(frame_Key,font=("Times New Roman",15),width=5)
    entry_k.pack(side=LEFT,padx=10)
    
    #Đọc dư liệu key ngày hôm nay
    data_k = ''
    try:
        f = open(".\\key\\" + today + ".txt", 'r')
        data_k = f.read()
    except:
        data_k = ''
    scrollbar_KeyX = Scrollbar(tabKey,orient=HORIZONTAL)
    scrollbar_KeyY = Scrollbar(tabKey)
    text_Key = Text(tabKey,font=("Times New Roman",15),width=70,height=300, wrap = NONE,xscrollcommand = scrollbar_KeyX.set,yscrollcommand = scrollbar_KeyY.set)

    #Nút để hiển thị danh sách phím cho ngày đã nhập
    Button(frame_Key, text="Chọn",font=("Times New Roman",15),command=lambda: XemKeyNgayKhac(tabKey, text_Key ,entry_k.get()),width=5, background="#C4C4C4").pack(side=LEFT,padx=10)
    
    #Chi data key để hiển thị
    scrollbar_KeyY.pack(side = RIGHT, fill = Y)
    scrollbar_KeyX.pack(side = BOTTOM, fill = X)
    text_Key.insert(END, data_k)

    text_Key.pack(fill=Y)
    scrollbar_KeyX.config(command=text_Key.xview)
    scrollbar_KeyY.config(command=text_Key.yview)
    text_Key['state'] = 'disabled'

    # p.resizable(0,0)
    p.mainloop()
    p.quit()

#-------------------------------Hàm sử dụng cho tabKhungGio-----------------------------------------
#Hàm update khung giờ
def update(text_KhungGio, label_khungGio):
    data = readFileText()
    text_KhungGio['state'] = 'normal'
    text_KhungGio.delete("1.0","end")
    text_KhungGio.insert(END,"FROM\tTO\tDURATION\t\tINTERRUPT TIME\t\t\tSUM\n\n")
    for i in range(len(data)):
        text_KhungGio.insert(END, data[i]['F'] + '\t' + data[i]['T'] + '\t' + str(data[i]['D']) + '\t\t' + str(data[i]['I']) + '\t\t\t' + str(data[i]['S']) + '\n\n')
    text_KhungGio['state'] = 'disabled'
    label_khungGio.after(1000, lambda: update(text_KhungGio, label_khungGio))


#Hàm hiển thị danh sách muốn thay mật khẩu (Gồm child và parent)
def ChangePassword():
    pw = Toplevel(bg="#FFFFFF")
    pw.title("Đổi mật khẩu")
    pw.geometry("200x200+500+200")
    pw.resizable(0,0)

    Button(pw, text="Child ",font=("Times New Roman",15),command=lambda: ChangePasswordForChild(pw), background="#C4C4C4").pack(padx=20,pady=20)
    Button(pw, text="Parent",font=("Times New Roman",15),command=lambda: ChangePasswordForParent(pw), background="#C4C4C4").pack(padx=20,pady=20)

#Hàm hiển thị form nhập mật khẩu mới để thay đổi mật khẩu cho con
def ChangePasswordForChild(pw):
    pw.destroy()
    pw_child = Toplevel(bg="#FFFFFF")
    pw_child.title("Đổi mật khẩu cho tài khoản trẻ")
    pw_child.geometry("300x200+500+200")
    pw_child.resizable(0,0)
    Label(pw_child,text="New password", font=("Times New Roman",15),padx = 10,pady = 10,background="#FFFFFF").pack()
    entry = Entry(pw_child,font=("Times New Roman",15))
    entry.pack(padx = 10,pady = 10)
    Button(pw_child, text="Xác Nhận",font=("Times New Roman",15),command=lambda: ChangePasswordInData('c',pw_child,entry.get(),entry),background="#13857D").pack(padx=20,pady=20)

#Hàm hiển thị form nhập mật khẩu mới để thay đổi mật khẩu cho cha
def ChangePasswordForParent(pw):
    pw.destroy()
    pw_parent = Toplevel(bg="#FFFFFF")
    pw_parent.title("Đổi mật khẩu cho tài khoản dhq")
    pw_parent.geometry("300x200+500+200")
    pw_parent.resizable(0,0)
    Label(pw_parent,text="New password", font=("Times New Roman",15),padx = 10,pady = 10,background="#FFFFFF").pack()
    entry = Entry(pw_parent,font=("Times New Roman",15))
    entry.pack(padx = 10,pady = 10)
    Button(pw_parent, text="Xác Nhận",font=("Times New Roman",15),command=lambda: ChangePasswordInData('p',pw_parent,entry.get(),entry),background="#13857D").pack(padx=20,pady=20)

#Hàm thay đổi mật khẩu trong file user.dat
def ChangePasswordInData(t,pw,pw_text,entry):
    if pw_text == '' or len(pw_text.split(' ')) > 1:
        Label(pw,text="KHÔNG HỢP LỆ", font=("Times New Roman",15),padx = 10,pady = 10,background="#FFFFFF",fg="#D03838").pack()
        entry.delete(0,END)
        return
    pw.destroy()

    f = open("./data/user.dat","rb")
    data = f.read().decode()
    data_list = data.split('\n')
    if t == 'c':
        data_list[0] = 'c' + pw_text
    else:
        data_list[1] = 'p' + pw_text
    with open("./data/user.dat","wb") as f1:
        s = data_list[0] +'\n'+data_list[1]
        f1.write(s.encode())
        
    pw1 = Toplevel(bg="#87faa1")
    pw1.geometry("300x150+500+200")
    label = Label(pw1,text="THÀNH CÔNG", font=("Times New Roman",30),padx = 20,pady = 50, bg="#87faa1",fg="#03bc2c")
    label.pack()
    label.after(1000,pw1.destroy)

#Hàm đọc file khung giờ
def readFileText():
    f = open(".\\text.txt", 'r')
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

#Hàm ghi lại data vào file khung giờ
def writeFile(data):
    with open(".\\text.txt", 'w') as f:
        for data1 in data:
            f.write('F' + data1['F'] + ' ')
            f.write('T' + data1['T'])

            if data1['D'] != '' and data1['D'] != None:
                f.write(' D' + data1['D'])
            if data1['I'] != '' and data1['I'] != None:
                f.write(' I' + data1['I'])
            if data1['S'] != '' and data1['S'] != None:
                f.write(' S' + data1['S'])
            f.write('\n')

# Hàm xử lí đụng độ khi ghi file
def writeFileText(data):
    senaphore = None
    with open(".\\flag.txt", mode='r') as f:
        senaphore = int(f.read())
    if senaphore != 1:
        time.sleep(1)
        writeFileText(data)
    else:
        senaphore = threading.Semaphore(senaphore)
        
        senaphore.acquire()
        with open("flag.txt", mode='w') as f:
            f.write(str(senaphore._value))

        writeFile(data)


        senaphore.release()
        with open("flag.txt", mode='w') as f:
            f.write(str(senaphore._value))

#Hàm hiển thị form điểu chỉnh khung giờ (nhập khung giờ bắt đầu đề biết chỉnh sửa khung giờ nào)
def DieuChinh(text_KhungGio, data, act):
    if act == 't':
        DieuChinhInText(None, text_KhungGio, '','',data,None,act)
        return
    dc = Toplevel(bg="#FFFFFF")
    dc.title("Khung giờ")
    dc.geometry("300x250+500+200")
    dc.resizable(0,0)
    Label(dc,text="Thời gian bắt đầu", font=("Times New Roman",15), background = "#FFFFFF").pack()
    dc_frame = Frame(dc,background = "#FFFFFF")
    dc_frame.pack()
    entry = Entry(dc_frame,font=("Times New Roman",15),width=5)
    entry1 = Entry(dc_frame,font=("Times New Roman",15),width=5)
    entry.pack(side=LEFT,padx=10)
    Label(dc_frame,text=":", font=("Times New Roman",15), background = "#FFFFFF").pack(side=LEFT,padx=10)
    entry1.pack(side=LEFT,padx=10)
    error ={"error" : None}
    error["error"] = Label()
    Button(dc, text=" Xác nhận ", font=("Times New Roman",15),command= lambda: DieuChinhInText(dc, text_KhungGio, entry.get() , entry1.get(), data, error, act), background="#7AB49B").pack(pady=15)

#Hàm hiển thị form nhập các thông tin để chỉnh sửa
def DieuChinhInText(dc, text_KhungGio, h , p, data,error,act):
    if act == 'x':
        data = readFileText()
        for i in range(len(data)):
            if h + ':' + p == data[i]['F']:
                data.pop(i)
                writeFileText(data)
                dc.destroy()
                text_KhungGio['state'] = 'normal'
                text_KhungGio.delete("1.0","end")
                text_KhungGio.insert(END,"FROM\tTO\tDURATION\t\tINTERRUPT TIME\t\t\tSUM\n\n")
                for i in range(len(data)):
                    text_KhungGio.insert(END, data[i]['F'] + '\t' + data[i]['T'] + '\t' + str(data[i]['D']) + '\t\t' + str(data[i]['I']) + '\t\t\t' + str(data[i]['S']) + '\n\n')
                text_KhungGio['state'] = 'disabled'
                return

        error['error'].destroy()
        error['error'] = Label(dc,text="KHÔNG HỢP LỆ", font=("Times New Roman",15), background = "#FFFFFF",fg="#D03838")
        error['error'].pack(pady=10)
        return
    if act == 't':
        dc1 = Toplevel(bg="#FFFFFF")
        dc1.title("Khung giờ")
        dc1.geometry("300x480+500+200")
        dc1.resizable(0,0)
        dc1_frame1 = Frame(dc1,bg="#FFFFFF")
        dc1_frame2 = Frame(dc1,bg="#FFFFFF")

        Label(dc1,text="FROM", font=("Times New Roman",15), background = "#FFFFFF").pack()
        dc1_frame1.pack()

        entry_F1 = Entry(dc1_frame1,font=("Times New Roman",15),width=5)
        entry_F2 = Entry(dc1_frame1,font=("Times New Roman",15),width=5)
        entry_F1.pack(side=LEFT,padx=10)
        Label(dc1_frame1,text=":", font=("Times New Roman",15), background = "#FFFFFF").pack(side=LEFT,padx=10)
        entry_F2.pack(side=LEFT,padx=10)

        Label(dc1,text="TO", font=("Times New Roman",15), background = "#FFFFFF").pack() 
        dc1_frame2.pack()

        entry_T1 = Entry(dc1_frame2,font=("Times New Roman",15),width=5)
        entry_T2 = Entry(dc1_frame2,font=("Times New Roman",15),width=5)
        entry_T1.pack(side=LEFT,padx=10)
        Label(dc1_frame2,text=":", font=("Times New Roman",15), background = "#FFFFFF").pack(side=LEFT,padx=10)
        entry_T2.pack(side=LEFT,padx=10)

        Label(dc1,text="DURATION", font=("Times New Roman",15), background = "#FFFFFF").pack() 
        entry_D = Entry(dc1,font=("Times New Roman",15),width=15)
        entry_D.pack()

        Label(dc1,text="INTERRUPT TIME", font=("Times New Roman",15), background = "#FFFFFF").pack() 
        entry_I = Entry(dc1,font=("Times New Roman",15),width=15)
        entry_I.pack()

        Label(dc1,text="SUM", font=("Times New Roman",15), background = "#FFFFFF").pack() 
        entry_S = Entry(dc1,font=("Times New Roman",15),width=15)
        entry_S.pack()
        error1 = {'error': None}
        error1['error'] = Label()
        Button(dc1, text=" Xác nhận ", font=("Times New Roman",15),command= lambda: DieuChinhInText2(dc1, text_KhungGio, None, entry_F1.get() +':'+ entry_F2.get() ,entry_T1.get()+':'+entry_T2.get() , entry_D.get(),entry_I.get(),entry_S.get(),error1, act), background="#7AB49B").pack(pady=15)
        return

    for i in range(len(data)):
        if h + ':' + p == data[i]['F']:
            dc.destroy()
            dc1 = Toplevel(bg="#FFFFFF")
            dc1.title("Khung giờ")
            dc1.geometry("300x480+500+200")
            dc1.resizable(0,0)
            dc1_frame1 = Frame(dc1,bg="#FFFFFF")
            dc1_frame2 = Frame(dc1,bg="#FFFFFF")

            Label(dc1,text="FROM", font=("Times New Roman",15), background = "#FFFFFF").pack()
            dc1_frame1.pack()

            entry_F1 = Entry(dc1_frame1,font=("Times New Roman",15),width=5)
            entry_F2 = Entry(dc1_frame1,font=("Times New Roman",15),width=5)
            entry_F1.pack(side=LEFT,padx=10)
            Label(dc1_frame1,text=":", font=("Times New Roman",15), background = "#FFFFFF").pack(side=LEFT,padx=10)
            entry_F2.pack(side=LEFT,padx=10)

            Label(dc1,text="TO", font=("Times New Roman",15), background = "#FFFFFF").pack() 
            dc1_frame2.pack()

            entry_T1 = Entry(dc1_frame2,font=("Times New Roman",15),width=5)
            entry_T2 = Entry(dc1_frame2,font=("Times New Roman",15),width=5)
            entry_T1.pack(side=LEFT,padx=10)
            Label(dc1_frame2,text=":", font=("Times New Roman",15), background = "#FFFFFF").pack(side=LEFT,padx=10)
            entry_T2.pack(side=LEFT,padx=10)

            Label(dc1,text="DURATION", font=("Times New Roman",15), background = "#FFFFFF").pack() 
            entry_D = Entry(dc1,font=("Times New Roman",15),width=15)
            entry_D.pack()

            Label(dc1,text="INTERRUPT TIME", font=("Times New Roman",15), background = "#FFFFFF").pack() 
            entry_I = Entry(dc1,font=("Times New Roman",15),width=15)
            entry_I.pack()

            Label(dc1,text="SUM", font=("Times New Roman",15), background = "#FFFFFF").pack() 
            entry_S = Entry(dc1,font=("Times New Roman",15),width=15)
            entry_S.pack()
            error1 = {'error': None}
            error1['error'] = Label()
            Button(dc1, text=" Xác nhận ", font=("Times New Roman",15),command= lambda: DieuChinhInText2(dc1, text_KhungGio, i, entry_F1.get() +':'+ entry_F2.get() ,entry_T1.get()+':'+entry_T2.get() , entry_D.get(),entry_I.get(),entry_S.get(),error1, act), background="#7AB49B").pack(pady=15)
            
            return
    error['error'].destroy()
    error['error'] = Label(dc,text="KHÔNG HỢP LỆ", font=("Times New Roman",15), background = "#FFFFFF",fg="#D03838")
    error['error'].pack(pady=10)

#Hàm chỉnh sửa khung giờ trong file text với dữ liệu đã nhập và hiện thị ra màn hình
def DieuChinhInText2(dc1, text_KhungGio,indexInData, F, T, D, I, S,error1,act):
    if checkTime(F) == False or checkTime(T) == False or checkInt(D) == False or checkInt(I) == False or checkInt(S) == False:
        error1['error'].destroy()
        error1['error'] = Label(dc1,text="KHÔNG HỢP LỆ", font=("Times New Roman",15), background = "#FFFFFF",fg="#D03838")
        error1['error'].pack(pady=10)
        return
    data = readFileText()
    if act == 't':
        data.append({'F': F,'T': T,'D': D,'I': I,'S':S})
    else:
        data[indexInData]['F'] = F
        data[indexInData]['T'] = T
        data[indexInData]['D'] = D
        data[indexInData]['I'] = I
        data[indexInData]['S'] = S 
    writeFileText(data)

    data = readFileText()
    text_KhungGio['state'] = 'normal'
    text_KhungGio.delete("1.0","end")
    text_KhungGio.insert(END,"FROM\tTO\tDURATION\t\tINTERRUPT TIME\t\t\tSUM\n\n")
    for i in range(len(data)):
        text_KhungGio.insert(END, data[i]['F'] + '\t' + data[i]['T'] + '\t' + str(data[i]['D']) + '\t\t' + str(data[i]['I']) + '\t\t\t' + str(data[i]['S']) + '\n\n')
    text_KhungGio['state'] = 'disabled'
    dc1.destroy()

#-------------------------------Hàm sử dụng cho tabLichSu-----------------------------------------
#Hàm đọc lịch sử ngày đã nhập vào Entry và ghi ra
def XemLichSuNgayKhac(tabLichSu ,text_LichSu,time):
    if checkDate(time) == False:
        return
    try:
        f = open(".\\history_time\\" + time + ".txt", 'r')
        data_ls = f.read().split('\n')
    except:
        data_ls = []

    text_LichSu['state'] = 'normal'
    text_LichSu.delete("1.0","end")
    text_LichSu.insert(END,"\t\tFROM\t\t\t\tTO\n\n")
    for i in range(len(data_ls)):
        if data_ls[i] != '':
            text_LichSu.insert(END, '\t\t' + data_ls[i].split('~')[0] + '\t\t\t\t' + data_ls[i].split('~')[1] + '\n\n')

    text_LichSu['state'] = 'disabled'

#-------------------------------Hàm sử dụng cho tabHinhAnh-----------------------------------------
#Hàm xuất hình ảnh kế tiếp
def HinhAnhKeTiep(frame_HinhAnh3,H):
    if H['index_images'] >= len(H['images']) - 1:
        return
    H['image_label'][H['index_images']].destroy()
    H['index_images'] += 1
    H['image_label'][H['index_images']] = Label(frame_HinhAnh3, image=H['images'][H['index_images']])
    H['image_label'][H['index_images']].pack(side=LEFT,pady=20)
    
#Hàm xuất hình ảnh trước đó
def HinhAnhTruoc(frame_HinhAnh3, H):
    if H['index_images'] <= 0:
        return

    H['image_label'][H['index_images']].destroy()
    H['index_images'] -= 1
    H['image_label'][H['index_images']] = Label(frame_HinhAnh3, image=H['images'][H['index_images']])
    H['image_label'][H['index_images']].pack(side=LEFT,pady=20)

#Hàm xuất tập hình ảnh ngày khác
def XemHinhAnhNgayKhac(frame_HinhAnh3,H, time):
    if checkDate(time) == False:
        return

    for i in range(len(H['image_label'])):
        if H['image_label'][i] != None:
            H['image_label'][i].destroy()

    for i in range(len(H['images'])):
        H['images'].pop(-1)
        H['image_label'].pop(-1)

    H['index_images'] = 0

    for file in glob.glob(".\\image\\"+ time +"\\*"):
        try:
            image = Image.open(file)
        except:
            continue
        resize_image = image.resize((879,500))
        Image2 = ImageTk.PhotoImage(resize_image)
        H['images'].append(Image2)

    if len(H['images']) != 0:

        for i in range(len(H['images'])):
            H['image_label'].append(None)

        H['image_label'][H['index_images']] = Label(frame_HinhAnh3, image=H['images'][H['index_images']])
        H['image_label'][H['index_images']].pack(side=LEFT,pady=20)

#-------------------------------Hàm sử dụng cho tabKey-----------------------------------------
#Hàm xuất key ngày đã nhập vào Entry
def XemKeyNgayKhac(tabKey, text_Key ,time):
    if checkDate(time) == False:
        return

    data_k = ''
    try:
        f = open(".\\key\\" + time + ".txt", 'r')
        data_k = f.read()
    except:
        data_k = ''

    text_Key['state'] = 'normal'
    text_Key.delete("1.0","end")
    text_Key.insert(END, data_k)
    text_Key['state'] = 'disabled'


#-------------------------------Hàm sử dụng cho việc check các dữ liệu nhập vào-----------------------------------------
#Hàm kiểm tra dữ liệu có phù hợp với thời gian
def checkTime(time):
    if len(time)!= 5:
        return False
    try:
        time1 = time.split(':')
        if int(time1[0]) >= 24 or int(time1[0]) < 0:
            return False
        if int(time1[1]) >= 60 or int(time1[1]) < 0:
            return False
    except:
        return False
    return True

#Hàm check Int
def checkInt(val):
    if val == '':
        return True
    try:
        int(val)
    except:
        return False
    return True
    
#Hàm kiểm tra dữ liệu có phải dạng date 'd-m'
def checkDate(d):
    try:
        if int(d.split('-')[0]) > 31 or int(d.split('-')[0]) <= 0:
            return False
        if int(d.split('-')[1]) > 12 or int(d.split('-')[1]) <= 0:
            return False
    except:
        return False
    return True

if __name__ == '__main__':
    Parent()
    