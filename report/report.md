# ĐỒ ÁN CUỐI KÌ HỆ ĐIỀU HÀNH 19_3

**GIÁO VIÊN HỖ TRỢ: Thái Hùng Văn** 

---

# Table conttent

---

# Thông tin thành viên và bài phân công công việc

**CÔNG VIỆC CHUNG**

$\color{ff} \rule{150px}{3px}$

- Tìm hiểu tài liệu
- Bàn luận hướng giải quyết từng câu hỏi
- Họp bàn đồ án hằng ngày
- Cùng hoàn thành báo cáo.

**HỌ TÊN**

$\color{deadf} \rule{84px}{3px}$

LÊ ANH VŨ

$\color{deadf} \rule{84px}{3px}$

NGÔ MẬU TRƯỜNG

**MSSV**

$\color{deadf} \rule{57px}{3px}$

19120724

$\color{deadf} \rule{57px}{3px}$

19120699

**CÔNG VIỆC RIÊNG**

$\color{ff} \rule{177px}{3px}$

- Hoàn thành các ý chính câu 1
- Các hàm chức năng câu 2 (các chức năng trong C2.1.1, C2.1.2.2)
- Xử lí vùng găng
- Edit video demo

$\color{ff} \rule{177px}{3px}$

- Kiểm tra, chỉnh sửa câu 1
- Đảm nhận xây dựng GUI, các chức năng còn lại trong Câu 2.
- Demo video

$\color{ff} \rule{550px}{3px}$

# Các chức năng và mức độ hoàn thành.

| Nhiệm vụ | Độ hoàn thành  |
| --- | --- |
| Câu 1 | 100% |
| Câu 2 C0 | 100% |
| Câu 2 C1 | 100% |
| Câu 2 C2.1.1 | 100% |
| Câu 2 C2.1.2.1 | 100% |
| Câu 2 C2.1.2.2 | 100% |
| Câu 2 P | 100% |

# 1. Câu 1

## 1.1 **Bộ nhớ ảo (Vitural memory)**

Bộ nhớ ảo là sự trừu tuợng hóa của HĐH, nó cung cấp cho người lập trình một không gian địa chỉ lớn hơn không gian địa chỉ vật lý thực sự. Bộ nhớ ảo được thiết kế để kết hợp giữa RAM và dung lượng trên đĩa cứng.

Điều này có nghĩa là khi RAM sắp hết, bộ nhớ ảo có thể di chuyển dữ liệu từ nó sang một không gian được gọi là paging file hoặc swap file (linux). Quá trình này cho phép giải phóng RAM để máy tính có thể hoàn thành tác vụ.

Bộ nhớ ảo có thể được triển khai bằng cách phân trang hoặc phân đoạn. 

Lợi ích của bộ nhớ ảo:

- Lập trình viên không lo lắng với việc các máy tính khác nhau có kích thước bộ nhớ vật lý khác nhau.
- Phân mảnh trong môi trường đa trương,

## 1.2 **Phân trang**

### 1.2.1 Cơ chế phân trang

Cơ chế phân trang như sau. Một địa chỉ logic bao gồm hai phần, phần biểu diễn **vị trí page** và biểu diễn **vị trí phần tử** trong một page. Mọi thôi tin được lưu trong bảng mô tả ánh xạ **page table.** Từ đó có thể suy ra được địa chỉ vật lý. **NOTE**: khác với phân đoạn, mỗi trang trong phân trang có kích thước bằng nhau.

![Figure 1.1 Cơ chế phân trang](%C4%90O%CC%82%CC%80%20A%CC%81N%20CUO%CC%82%CC%81I%20KI%CC%80%20HE%CC%A3%CC%82%20%C4%90IE%CC%82%CC%80U%20HA%CC%80NH%2019_3%2094acd8e88dd34771919de281ae2a2eba/Untitled.png)

Figure 1.1 Cơ chế phân trang

### 1.2.2 Ánh xạ

Trong việc ánh xạ từ **Logical memory** đến **Physical memory**, cần làm rõ các điều sau:

- Ở bộ nhớ vật lý được chia thành các **frame,** có kích thước đúng bằng một page trong bộ nhớ ảo.
- Việc ánh xạ từ bộ nhớ ảo bằng cách so khớp với thông tin trong bảng mô tả **page table. Ví dụ** trong hình biên dưới, page số 0 sẽ nằm ở frame thứ 1, page 1 tương ứng frame 4.

![Figure 1.2 Phương thức ánh xạ.](%C4%90O%CC%82%CC%80%20A%CC%81N%20CUO%CC%82%CC%81I%20KI%CC%80%20HE%CC%A3%CC%82%20%C4%90IE%CC%82%CC%80U%20HA%CC%80NH%2019_3%2094acd8e88dd34771919de281ae2a2eba/Untitled%201.png)

Figure 1.2 Phương thức ánh xạ.

### 1.2.3 Địa chỉ ảo.

Địa chỉ luận lý gồm có:

- Số hiệu trang (**Page number**) p
- Địa chỉ tương đối trong trang (**Page offset**) d

Nếu kích thước của không gian địa chỉ luận lý là $2^m$, và kích thước của trang là $2^n$  (đơn vị là byte hay word tùy theo kiến trúc máy) thì bảng phân trang sẽ có tổng cộng $2^m / 2^n = 2^{m-n}$  mục (entry)

![Figure 1.3 Địa chỉ ảo.](%C4%90O%CC%82%CC%80%20A%CC%81N%20CUO%CC%82%CC%81I%20KI%CC%80%20HE%CC%A3%CC%82%20%C4%90IE%CC%82%CC%80U%20HA%CC%80NH%2019_3%2094acd8e88dd34771919de281ae2a2eba/Untitled%202.png)

Figure 1.3 Địa chỉ ảo.

## 1.3 Khảo sát thực tế trên hệ thống máy tính x86_64

Ở phần này em khảo sát trên máy tính cá nhân của em. Máy sử dụng kiến trúc x86_64 trên nhân linux.

![Figure 1.4 Thông tin máy tính cá nhân,](%C4%90O%CC%82%CC%80%20A%CC%81N%20CUO%CC%82%CC%81I%20KI%CC%80%20HE%CC%A3%CC%82%20%C4%90IE%CC%82%CC%80U%20HA%CC%80NH%2019_3%2094acd8e88dd34771919de281ae2a2eba/Untitled%203.png)

Figure 1.4 Thông tin máy tính cá nhân,

Dựa trên các thông tin từ hệ điều hành cung cấp cùng các thông tin mặc định của kiến trúc x86_64. Em nhận được các thông số như sau.

**Page size:** Em sử dụng lệnh `pagesize` ****để kiểm tra kích thước mỗi page. Theo như kết quả trả về đó là 4096 Byte, đồng nghĩa **frame size** cũng là 4096 Byte

![Figure 1.5 Page size.](%C4%90O%CC%82%CC%80%20A%CC%81N%20CUO%CC%82%CC%81I%20KI%CC%80%20HE%CC%A3%CC%82%20%C4%90IE%CC%82%CC%80U%20HA%CC%80NH%2019_3%2094acd8e88dd34771919de281ae2a2eba/Untitled%204.png)

Figure 1.5 Page size.

**Kích thước bộ nhớ ảo:** RAM + swap space = 8106180608 + 4828688384 =  12934868992 (bytes)

**Số khung trang vật lý:** Số bytes trên RAM / page size = 8106180608 / 4096 = 1979048 (bytes)

---

Các thông số trên là những thứ em có thể lấy từ máy tính. Đến phần tiếp theo em dựa vào thông tin trên [kernel linux](https://github.com/torvalds/linux/find/master). Intel `x86_64` có số địa chỉ thực chất chỉ 48 bits (16 bit trên không đuợc sử dụng và định nghĩa giá trị), 48 bit địa chỉ ảo được biễu diễn như sau:

| 9 bit PML4I
 (page map level 4 index) | 9 bit PDPTI
 (page directory pointer table index) | 9 bit PDI
 (page directory index) | 9 bit PTI
 (page table index) | 12 bit offset |
| --- | --- | --- | --- | --- |

---

**Số bit tối thiểu để quản lí các offset trong trang:** Là số bit cần thiết để đánh só các địa chỉ trong page. Ta đã có pagesize là 4096 bytes. Vậy ta cần ít nhất 12 bit để đánh các offset. Hợp lý với bảng biễu diễn trên.

**Số bit quản lí ô nhớ:** 48 bits

**Số frame logic tối đa trên không gian tiến  trình:**

- Theo lý thuyết số frame tối đa sẽ bằng  $2^{\text{bit biễu diễn địa chỉ logic}} / \text{pagesize} = 2^{48} /  2^{12} = 2^{36} \text{ frame}$
- Nhưng theo Document của linux `user-space virtual memory` chỉ có 128 TB. Vậy số frame tối đa trên `x86_64` là $2^{47} / 2^{12} = 2^{35} \text{ frame}$.

```
====================================================
Complete virtual memory map with 4-level page tables
====================================================

Notes:

 - Negative addresses such as "-23 TB" are absolute addresses in bytes, counted down
   from the top of the 64-bit address space. It's easier to understand the layout
   when seen both in absolute addresses and in distance-from-top notation.

   For example 0xffffe90000000000 == -23 TB, it's 23 TB lower than the top of the
   64-bit address space (ffffffffffffffff).

   Note that as we get closer to the top of the address space, the notation changes
   from TB to GB and then MB/KB.

 - "16M TB" might look weird at first sight, but it's an easier to visualize size
   notation than "16 EB", which few will recognize at first sight as 16 exabytes.
   It also shows it nicely how incredibly large 64-bit address space is.

========================================================================================================================
    Start addr    |   Offset   |     End addr     |  Size   | VM area description
========================================================================================================================
                  |            |                  |         |
 0000000000000000 |    0       | 00007fffffffffff |  128 TB | user-space virtual memory, different per mm
```

---

**Tài liệu tham khảo**

[linux/mm.rst at master · torvalds/linux](https://github.com/torvalds/linux/blob/master/Documentation/x86/x86_64/mm.rst)

[Paging on Intel x86-64](https://www.iaik.tugraz.at/teaching/materials/os/tutorials/paging-on-intel-x86-64/)

---

# 2. Câu 2

## 2.1 Ý tưởng thiết kế

**Theo yêu cầu của đề bài, chúng em lên ý tưởng thiết kế sàn phẩm như sau:**

- **Ứng dụng đồ hoạ, thân thiện với người dùng:** Vì là một sản phẩm có tính ứng dụng và thực tiễn, cho nên chúng em quyết định xây dựng một phần mềm ứng dụng đồ hoạ. Bên cạnh đó, mục tiêu sản phẩm là dành cho quản lí trẻ em, nên sản phẩm phải thân thiện, dễ sử dụng.
- **Áp dụng các kiến thức về quản lí tiến trình, đồng bộ hoá**: Vì là đồ án môn HDH, do đó chúng em áp dụng các kiến thức về quản lí tiến trình và đồng bộ hoá vào sản phẩm.
- **Áp dụng ổ đĩa ảo**: Áp dụng ổ đỉa ảo để lưu trữ và đồng bộ dữ liệu trong quá trình sử dụng.

**Các công nghệ, thư viện mà bọn em sử dụng:**

- **Ổ đĩa ảo:** One Drive.
- **Ngôn ngữ lập trình:** `python`
- **Các thư viện**:
    - `tkinter` : dùng để tạo đồ hoạ
    - `PIL, Pillow` : dùng thao tác với file dạng ảnh
    - `glob` : đọc thư mục
    - `threading` : dùng để tạo các tiểu trình song song.
    - `time, datetime` : dùng để thao tác với dữ liệu thời gian
    - `gTTS,  playsound` : dùng để tạo các thông báo âm thanh
    - `pyautogui, pynput` : dùng để theo dõi hình ảnh và key của trẻ.
    

**Cấu trúc file code và file, thư mục dữ liệu**:

```markdown
root
		|
		data
				|
				history # Dùng để chứa các file chứa thời gian sum còn lại của chương trình
				|     |
				|     interrupt.txt # Dùng để chứa thời điểm được phép sử dụng 
				|			              # (đề phòng trường hợp trong khoảng interrupt, 
				|										# trẻ tắt máy rồi bật lại)
				|
				user.dat # Dùng để chứa mật khẩu
				|
				status.txt # Dùng để chứa thời gian cho phép đăng nhập (nếu như mật khẩu sai lần thứ 3) 
		history_time # Dùng để lưu lịch sử sử dụng của trẻ
		|
		image # Dùng để chứa các file hình ảnh được chụp khi trẻ sử dụng máy
		|
		key # Dùng để chứa các file theo dõi key mà trẻ nhập
		|
    background.jpg # Chứa hình ảnh nền cho chương trình lấy mật khẩu
		|
		C.py # Chứa hàm thực thi chứa năng của chương trình C (khi đăng nhập thành công)
		|
		P.py # Chương trình P
		|
		thong_bao_thoi_gian.py # Dùng để xây dựng các hàm xử lí thời gian
		|
		Main.py # Chương trình C 
		|
		text.txt # Chứa các thông tin khung giờ sử dụng
		|
		flag.txt # Chứa giá trị cờ hiệu để xứ lí đồng bộ
		
```

## 2.2 Sơ bộ về chương trình Child và Parent

### 2.2.1 Chương trình Child

- **C0**: Lấy mật khẩu
- **C1**: Nhập mật khẩu phụ huynh thì phụ huynh sử dụng và 60p sau thì quay lại bước C0
- **C2**: Không phải phụ huynh
    - **C2.1**: Kiểm tra xem thời điểm hiện tại có nằm trong khung thời gian trẻ chưa được dùng máy hay không
        - **C2.1.1**: Nếu **KHÔNG** nằm trong thời gian trẻ sử dụng, Thông báo ra màn hình VÀ nói ra loa thời gian tiếp theo sử dụng, sau đó chờ 15s sau mới tắt máy, nếu trong thời gian 15s đó nhập đúng mật khẩu **Parent** thì sử dụng sau đó quay lại bước C0
        - **C2.1.2**: Nếu nằm trong thời gian trẻ sử dụng
            - **C2.1.2.1**: Không phải mật khẩu của trẻ, báo sai và nếu lần sai thứ 3 thì đặt thời gian không được dùng máy là 10 phút kể từ thời điểm hiện tại rồi tắt máy.
            - **C2.1.2.2**: Nếu là mật khẩu của trẻ, thực hiện chụp hình mỗi phút, lưu lại các phím đã bấm, đếm ngược đến khi kết thúc. Nếu thời gian đếm ngược còn 1p thì thông báo thời gian được phép sử dụng sắp tới, 0p thì tắt máy.

### 2.2.2 Chương trình Parent

Hiển thị 4 tab:

- **Tab Khung giờ:**
    - Hiển thị các khung giờ thông tin khung giờ trẻ có thể sử dụng
    - Điểu chỉnh khung giờ có thể chỉnh sửa thông vào khung giờ mình muốn chỉnh sửa
    - Thêm khung giờ sử dùng
    - Xóa khung giờ sử dụng
    - Có chức năng đổi mật khẩu cho các user ở tab này
    - Chức năng cập nhật khung giờ sử dụng mỗi giây (đồng bộ khi Parent khác thay đổi)
- **Tab Lịch sử:**
    - Hiển thị mắc định lịch sử sử dụng của trẻ ngày hiện tại
    - Chức năng xem lịch sử các ngày khác
- **Tab Hình ảnh:**
    - Hiển thị mắc định lịch sử hình ảnh của trẻ ngày hiện tại (mắc định hỉnh ảnh vị trí đầu được hiển thi)
    - Chức năng chuyển hình ảnh kế tiếp
    - Chức năng chuyển hỉnh ảnh trước
    - Chức năng xem hình ảnh các ngày khác
- **Tab Key:**
    - Hiển thị mắc định lịch sử phím của trẻ ngày hiện tại
    - Chức năng xem lịch sử phím các ngày khác

## 2.3 Thuật toán trong từng chức năng

### 2.3.1 C0: lấy mật khẩu

- **Hướng phát triển:**
    - Sử dụng thư viện `tkinter` để tạo giao diện
    - Sử dụng thư viện `Pillow` để tạo background
    - Lưu 1 file `user.dat` chứa mật khẩu các user, đọc file và so sánh với mật khẩu nhập vào
        - Cấu trúc file `user.dat`:
            
            ```markdown
            c<mật khẩu child>
            
            p<mật khẩu parent>
            ```
            
    - Thiết lập sau **1p** khi bật chương trình mà không nhập mật khẩu đúng thì tiến hành tắt máy (bắt buộc trẻ phải nhập mới sử dụng)
- **Thuật toán:**
    1. Lấy mật khẩu nhập vào
    2. Đọc file user
    3. Kiểm tra mật khẩu, nếu mật khẩu nhập vào là child thì chuyển đến chương trình Child, nếu mật khẩu nhập vào là parent thì chuyển đến hướng giải quyết cho parent, nếu không phải cả hai thì báo sai, xóa các kí tự đã nhập trong Entry và yêu cầu nhập lại

### 2.3.2 C1: Mật khẩu là phụ huynh

- **Hướng phát triển:**
    - Cho một vòng lặp chạy giao diện lấy mật khẩu, khi bấm vào nút đăng nhập nếu là mật khẩu phụ huynh thì lưu vào 1 biến (biến này lưu lại và cho biết người đăng nhập là Parent) thoát giao diện lấy mật khẩu.
    - Sau khi thoát giao diện lấy mật khẩu, kiểm tra biến, sau đó sleep chương trình 60 phút, rồi tiếp tục vòng lặp chạy giao diện lấy mật khẩu
- **Thuật toán:**
    1.  Khởi tạo biến lưu parent (Boolean)
    2.  Kiểm tra mật khẩu là parent thì  parent = True, thoát giao diện lấy mật khẩu
    3. Nếu `parent == True` thì ngủ 60 phút
    4. Sau 60 phút chạy lại giao diện lấy mật khẩu

### 2.3.3 C2.1: Kiểm tra có nằm trong khung giờ của trẻ

- **Hướng phát triển:**
    - Sử dụng thư viện `datetime` để so sánh thời gian
    - Dữ liệu đọc từ file khung giờ để so sánh có dạng `List` gồm nhiều `Dictionary`
    - Mỗi Dictionary gồm:
        
        ```python
        "F": from
        
        "T": to
        
        "D": duration
        
        "I": interrupt
        
        "S": sum
        
        Nếu "D", "I", "S" không tồn tại thì gắn bằng None
        ```
        

### 2.3.4 C2.1.1

- **Hướng phát triển:**
    - Sử dụng thư viện `gTTS`, `playsound`, `threading` để tạo và phát file mp3, sau khi đọc xong thì sử dụng thư viện `os` để xóa file mp3 (tạo file mp3 → phát file mp3 → xóa file mp3)
    - Khi tạo file mp3 rồi xóa nhiều lần sẽ gây ra lỗi hệ thống, giải quyết bằng cách lưu tên mỗi lần tạo khác nhau
    - Dùng threading để chạy `playsound` đến hết đề phòng trường hợp tắt khi đăng phát thông báo (có tạo biến stop thread khi thông báo giữa chừng thì mật khẩu Parent đăng nhập đúng)
    - Đề phòng trong khoảng thời gian loa thông báo, tiếp tục đăng nhập với mật khẩu không phải Parent nên tạo biến index_login cho biết có phải lần đầu bấm đăng nhập sai hay không (nếu là lần đăng nhập đầu thì thực hiện báo khung giờ tiếp theo, không thì bỏ qua)
    - Sử dụng câu lệnh `label.after` (`label` dùng để báo thời gian tiếp theo) để 15s thực hiện sau tắt chương trình
    - Lưu biến id của `label.after` để tắt lệnh 15s sau khi trong khoảng 15s nhập được mật khẩu parent
- **Thuật toán:**
    1. Nhấn đăng nhập, lấy chuỗi mật khẩu nhập vào
    2. `after_id` (lưu id của `label.after`), `stop_event` (biến dừng `thread`), `index_login` nhằm cho biết có phải lần đầu bấm đăng nhập sai
    3. Nếu không nằm trong khung giờ sử dụng → `index_login != 0` thì quay lại bước đầu, nếu ngược lại tiếp tục
    4. `index_login + = 1`
    5. Đọc thời gian tiếp theo cho phép sử dụng từ file khung giờ
    6. Chạy `thread` loa phát thông báo thời gian tiếp theo sử dụng và hiển thị thông báo đó ra màn hình (lưu lại biến `stop_event` để dừng `thread`)
    7. Đạt thời gian 15s sau thoát chương trình và lưu vào `after_id`
    8. Nếu trong khoảng 15s đó tiếp tục đăng nhập → nếu mật khẩu đăng nhập là `Parent` thì gắn `index_login = 0`, tắt sự kiện 15s sau thì tắt máy bằng `after_id`, `stop_event` để tắt thread đọc loa thông báo
    
    ```python
    #Kiểm tra xem có đang là trong khung giờ có thể sử dụng
            can_use = False
            for data1 in data:
                if datetime.strptime(data1['F'] + ':00','%H:%M:%S') <= t1 
    								\and t1 < datetime.strptime(data1['T'] + ':00','%H:%M:%S'):
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
    ```
    

### 2.3.5 C2.1.2.1: Không phải mật khẩu của trẻ mà trong khoảng thời gian sử dụng

- **Hướng phát triển:**
    - Tạo biến điếm `index_false_password` lưu số lần sai mật khẩu. Nếu sau 3 lần nhập mật khẩu không đúng, phải đợi 10p sau mới được phép đăng nhập lại.
    - Lưu thời gian 10 phút sau thời điểm hiện tại vào file, khi chạy chương trình sẽ xét file này để cho biết có chạy chương trình hay không.
    - Cấu trúc của file lưu là thời điểm được phép bật máy:
        
        `DD-MM hh:mm`
        

### 2.3.6 C2.1.2.2: Nếu mật khẩu đúng và trong thời gian trẻ sử dụng

- **Hướng phát triển:**
    - Dùng thư viện `tkinter` để tạo giao diện
    - Tạo đồng hồ đếm ngược khoảng thời gian dùng
    - Dùng thư viện `pyautogui` để chụp màn hình
    - Dùng thư viện `pynput` (dùng Key và Listener) để ghi lại các phím đã bấm
    - Dùng `threading` để chạy chức năng ghi lại các phím đã bấm
    - Lưu lại lịch sử dụng vào trong thư mục `history_time`, tên file lưu có dạng `‘DD-MM.txt’`, cấu trúc trong file dạng:
        
        ```
        <start1>~<end1>
        
        <start2>~<end2>
        
        …
        ```
        
    - Lưu lại ảnh chụp màn hình trong thư mục image, các hình ảnh được lưu trong thư mục có tên dạng ‘`DD-MM`’
    - Lưu lại các phím đã gõ vào thư mục key, tên file lưu có dạng ‘`DD-MM.txt`’
    - Lưu lại biến đếm ngược Sum (second) trong path có dạng ‘`data/history/<DD-MM>/<thời gian bắt đầu>.txt`’
    - Lưu lại biến `Intterupt` (thời gian được phép sử dụng sau quãng nghỉ tránh trường hợp trẻ tắt máy bật lại) trong thư mục data, và trong thư mục con history, tên file lưu là `interrupt.txt`. Trước khi chạy chương trình thì kiểm tra xem có nằm trong khoảng interrupt mới cho phép trẻ bật máy hay không.
- **Thuật toán :**
1. Đọc Sum, Duration (lưu lại thành second)  từ file khung giờ
2. Đọc file khung giờ
3. Kiểm tra xem có là lần chạy đầu chạy vòng lặp sự kiện 1s hay không, nếu phải thì lưu giờ hiện tại (ghi lịch sử sử dụng) vào file, nếu không ghì bỏ qua
4. Kiểm tra xem thời gian hiện tại có nằm trong khung giờ sử dụng hay không, nếu không thì thoát, nếu có thì tiếp tục
5. Tìm thời gian kết thúc:
    - Không tồn tại Sum: thời gian kết thúc là TO (thời gian kết thúc lưu trong file)
    - Tồn tại Sum:
        - Không tồn tại Duration, Interrupt:
            - Nếu thời gian TO nhỏ ****hơn thời gian hiện tại + SUM: thời gian kết thúc là TO
            - Ngược lại: thời gian kết thúc = thời gian hiện tại + SUM
        - Tồn tại Duration, Interrupt: tính index (số lần interrupt) bằng Sum/interrupt (để ước lượng thời điểm kết thúc dùng cho so sánh với TO) (nếu index là INT thì index -= 1)
            - Nếu thời gian TO nhỏ hơn thời gian hiện tại + SUM + index*interrupt: thời gian kết thúc là TO
            - Nếu ngược lại: thời gian kết thúc = thời gian hiện tại + SUM (bời vì trong khoảng nghỉ SUM không đếm ngược, tức là không cần tính cả interrupt vào)
6. Kiểm tra xem đã hết thời gian Duration hay chơi, nếu đã hết rồi, lưu Interrupt rồi ngủ máy 
7. Kiểm tra xem đã hết quãng Interrupt hay chưa, nếu chưa thì ’`try`’ ngủ máy (**ở đây phòng trường hợp trẻ  trong khoảng nghỉ bật máy thoát khỏi chế độ ngủ**):
    
    ```python
    #Nếu Interrupt lớn hơn thời gian hiện tại, tức là vẫn nằm trong thời gian Interrupt
    if Interrupt['I'] > datetime.today().time():
    
       #sleep system nếu như trẻ có ý định bật lại máy
       try:
           os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
       except:
           err = None
    ```
    
    Nếu ngược lại tức là có thể sử dụng máy thì khởi tạo lại biến đếm ngược Duration, xóa dữ liệu Interrupt đã lưu
    
8. Lưu thời gian đếm ngược = thời gian kết thúc – thời gian hiện tại
9. Nếu thời gian đếm ngược nhỏ hơn 1 phút thì xuất thời gian tiếp theo được bật máy, nếu nhỏ hơn 1s thì tắt máy , nếu ngược lại thì tiếp tục
10. Kiểm tra xem có sự thay đổi số phút trong label đã hiển thị ra trước đó hay không, nếu có thì chụp màn hình và lưu lại (thỏa mãn điều kiện một phút chụp màn hình một lần)
11. Hiển thị thời gian đếm ngược ra màn hình
12. Đếm ngược biến Sum và Duration (nếu có)
13. Đặt sự kiện 1s sau quay lại b2
14. Chạy `thread` ghi lại các phím đã bấm

### 2.3.7 P: Chức năng trong trương trình parrent

- **Hướng phát triển:**
    - Sử dụng thư viện `tkinter` để tạo giao diện
    - Sử dụng thư viện `Pillow` để đọc file ảnh
    - Sử dụng thư viện `glob` để đọc thư mục
    - Dùng thuật toán **semaphore** để giải quyết đụng độ
    - Dùng file `flag.txt` để chứa cờ hiệu
    
- **Thuật toán (semaphore):**
    1. Khi một chương trình Parent muốn chỉnh sửa file `text.txt` (dùng để chứa các khung giờ sử dụng) thì nó phải đọc file `flag.txt` trước.
    2. Nếu giá trị là 1, nghĩa là chưa có chương trình Parent nào đang chỉnh sửa. Thì ta sẽ thực hiện:
        - Ghi giá trị 0 vào `flag.txt`. Nhằm báo hiệu chương trình đang giành quyền sửa.
        - Thực hiện ghi file
        - Trả giá trị 1 vào `flag.txt` . Nhằm báo hiệu chương trình đã chỉnh sửa xong.
    3. Nếu giá trị là 0, nghĩa là chương trình Parent đang được chỉnh sửa. Thì ta thực hiện:
        - `sleep` chương trình trong vòng 1 giây.
        - Đệ quy lại hàm này
    
    ```python
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
    ```
    

## 2.4 Cài đặt autorun cho chương trình

**Có 2 cách cài đặt autorun cho chương trình:** 

1. sử dụng thư viện `Pyinstaller` để tạo file `.exe` sau đó tạo shortcut ở thư mục startup
2. tạo shortcut cmd chạy câu lệnh ở thư mục startup

**Ở đây chúng em lưu chọn phương án thứ hai:**

1. Bấm tổ hợp phím `window + R`, hộp thoại Run xuất hiện
2. Nhập `shell:startup` → `OK/Enter` → Thư mục startup xuất hiện

![Figure 2.1 Nhập `shell:startup`](%C4%90O%CC%82%CC%80%20A%CC%81N%20CUO%CC%82%CC%81I%20KI%CC%80%20HE%CC%A3%CC%82%20%C4%90IE%CC%82%CC%80U%20HA%CC%80NH%2019_3%2094acd8e88dd34771919de281ae2a2eba/Untitled%205.png)

Figure 2.1 Nhập `shell:startup`

1. Trong thư mục startup, nhấn chuột phải → New → shortcut → Hộp thoại tạo shortcut xuất hiện

![Untitled](%C4%90O%CC%82%CC%80%20A%CC%81N%20CUO%CC%82%CC%81I%20KI%CC%80%20HE%CC%A3%CC%82%20%C4%90IE%CC%82%CC%80U%20HA%CC%80NH%2019_3%2094acd8e88dd34771919de281ae2a2eba/Untitled%206.png)

1. Nhập `CMD /k python “<Đường dẫn file Child>` trong mục `Type the location of the item:` 

![Figure 2.2 Gán đường dẫn](%C4%90O%CC%82%CC%80%20A%CC%81N%20CUO%CC%82%CC%81I%20KI%CC%80%20HE%CC%A3%CC%82%20%C4%90IE%CC%82%CC%80U%20HA%CC%80NH%2019_3%2094acd8e88dd34771919de281ae2a2eba/Untitled%207.png)

Figure 2.2 Gán đường dẫn

1. Nhấn `Next` → Nhập tên mới cho shortcut → Nhấn `Finish`

![Figure 2.3  Đặt tên cho đường dẫn](%C4%90O%CC%82%CC%80%20A%CC%81N%20CUO%CC%82%CC%81I%20KI%CC%80%20HE%CC%A3%CC%82%20%C4%90IE%CC%82%CC%80U%20HA%CC%80NH%2019_3%2094acd8e88dd34771919de281ae2a2eba/Untitled%208.png)

Figure 2.3  Đặt tên cho đường dẫn

![Figure 2.4 Kết quả](%C4%90O%CC%82%CC%80%20A%CC%81N%20CUO%CC%82%CC%81I%20KI%CC%80%20HE%CC%A3%CC%82%20%C4%90IE%CC%82%CC%80U%20HA%CC%80NH%2019_3%2094acd8e88dd34771919de281ae2a2eba/Untitled%209.png)

Figure 2.4 Kết quả

## 2.5 Test

Phần test các chức năng được trình bày đầy đủ qua video. [Tại đây](https://youtu.be/p2L4PtKuG3w)

## 2.6 Tài liệu tham khảo

[How to detect key presses?](https://stackoverflow.com/questions/24072790/how-to-detect-key-presses)

[How to Take a Screenshot using Python](https://datatofish.com/screenshot-python/)

[Convert Text to Speech in Python - GeeksforGeeks](https://www.geeksforgeeks.org/convert-text-speech-python/)

[tkinter - Python interface to Tcl/Tk - Python 3.10.1 documentation](https://docs.python.org/3/library/tkinter.html)

[pynput](https://pynput.readthedocs.io/en/latest/)