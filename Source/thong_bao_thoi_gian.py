import os
from datetime import date, datetime, timedelta
import re #regular 

Path = {"P": os.path.dirname(os.path.abspath(__file__))}
history_path = Path['P'] + '\\data\\history'
name_dir_now = datetime.now().strftime("%d-%m")
history_today_path = f'{history_path}\\{name_dir_now}'


def use_time_datas(name_file):
    ''' () -> (lists)
    Define: Hàm này lấy list time_use để trả về khoảng thời gian sử dụng.
    '''
    
    '''
    Có 3 loại quy định thời gian
    [1] From - to - sum
    [2] From - to - duration - interrupt
    [3] From - to - duration - interrupt - sum 

    Loại From - to -> from - to - sum để bớt trường hợp.
    '''

    use_time_datas = []
    with open(name_file) as f: 

        for i in f:
            temp_dict = {}
            keys = re.findall('([A-Z])', i.rstrip())
            data = re.sub('[A-Z]', '', i.rstrip()).split()
            
            temp_dict[keys[0]] = datetime.strptime(data[0], "%H:%M").time()
            temp_dict[keys[1]] = datetime.strptime(data[1], "%H:%M").time()

            for j in range(2, len(keys)):
                temp_dict[keys[j]] = int(data[j])
            
            use_time_datas.append(temp_dict)

    return use_time_datas



def isin_use_time(now_time, use_time_datas):
    ''' (time, list) -> bool, integer
    Define: Hàm này dùng để check thời gian now_time có được phép sử dụng không
            now_time là định dạng time ("%H:%M")
    '''
    
    for i in range(len(use_time_datas)):
        
        if now_time >= use_time_datas[i]['F'] and now_time <= use_time_datas[i]['T']:
            return True, i

    return False

def readDuration(now_time, use_time_datas):
    '''
    Define:
    '''
    temp = use_time_datas[isin_use_time(now_time, use_time_datas)[1]]
    try:
        return temp['D']
    except:
        return None



def readInterrupt1(now_time, use_time_datas):
    '''
    Define: đọc thời gian intterupt
    '''
    temp = use_time_datas[isin_use_time(now_time, use_time_datas)[1]]
    try:
        return temp['I']
    except:
        return None


def readSum(now_time, use_time_datas):
    '''
    Define: đọc sum
    '''
    temp = use_time_datas[isin_use_time(now_time, use_time_datas)[1]]
    try:
        return temp['S'] * 60
    except:
        return None

def computeSum(now_time, use_time_datas):
    '''
    Define: chỉnh sum
    '''
    sum = readSum(now_time, use_time_datas)
    if sum == None:
        return None
    
    temp = use_time_datas[isin_use_time(now_time, use_time_datas)[1]]
    from_time = temp['F'].strftime("%H_%M")

    name_file = f"{history_today_path}\\{from_time}.txt"
    is_file = os.path.isfile(name_file)
    
    if is_file is True:
        with open(name_file) as f:
            sum = int(f.readline().rstrip())
        
    return sum

def next_use_time(now_time, use_time_datas):
    ''' (time, list) -> time
    Define: Hàm này dùng để trả về thời gian tiếp theo được sử dụng

    '''


    # Nếu now_time bé hơn một From(time) thì From đó là nextt.
    # Nếu now_time lớn hơn mọi From(time) thì trả về giá trị From nhỏ nhất.
    for i in use_time_datas:
        if now_time < i['F']:
            return i['F']
    return use_time_datas[0]['F']

def initializeInterrupt(now_time, use_time_datas):
    '''
    Define: ghi ra file thời gian hết sleep
    '''
    interrupt = readInterrupt1(now_time, use_time_datas)
    now_plus_inter = datetime.now() + timedelta(minutes=interrupt)
    
    with open(Path['P'] + "\\data\\history\\interrupt.txt", mode="w") as f:
        f.write(now_plus_inter.strftime("%d:%m %H:%M:%S"))

def  readInterrupt(file_name):
    '''
    Define: đọc thời điểm interrupt kết thúc.
    '''
    with open(file_name, mode="r") as f:
        temp = f.readline().rstrip()
        return temp

def save_sum(sum, use_time_datas):
    ''' file*, dict -> none
    Define: Hàm này dùng để in thông số thời gian.
    '''
    now_time = datetime.today().time()
    temp = use_time_datas[isin_use_time(now_time, use_time_datas)[1]]

    is_dir = os.path.isdir(history_today_path)

    if is_dir == False:
        os.makedirs(history_today_path)
    
    from_time = temp['F'].strftime("%H_%M")
    with open(f"{history_today_path}\\{from_time}.txt", mode="w") as f:
        f.write(str(sum))



