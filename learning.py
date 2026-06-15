
#__________________________________________________________________________________________________________________________________
# : List
score = [ 90, 80, 70 , 65, 48, 400, 600 ] #  

#Usually used to store a collection of data, such as a list of scores, names, or any other type of data.
score.append(67)            # them 1 phan tu vao cuoi list
score.insert(2, 78)        # them 1 phan tu vao vi tri chi dinh, cac phan tu sau se duoc dich chuyen sang phai
score.remove(48)           # xoa 1 phan tu trong list, neu co nhieu hon 1 phan tu trung nhau thi chi xoa phan tu dau tien                       
score.pop(4)               # xoa phan tu tai vi tri chi dinh, neu khong chi dinh thi mac dinh xoa phan tu cuoi cung
score.sort()             # sap xep theo thu tu tang dan, giam dan reverse = True vao ham sort
print(score)              #[65, 67, 70, 78, 80, 90, 400, 600]

#Phase 2: Nested List
gpa = [
    ["Elsa", 21, 3.5],
    ["Anna", 19, 3.2],
    ["Olaf", 13, 2.8]
]   # List chua cac list con, moi list con chua thong tin cua 1 nguoi
print(gpa[0][2]) #3.5
print(gpa[2][2]) #2.8

#Phase 3: Empty List, List Comprehension
name = [] # tao 1 list rong de chua ten cua moi nguoi trong list gpa
for student in gpa: # duyet qua tung list con trong list gpa, moi list con la thong tin cua 1 nguoi
    name.append(student[0]) # lay ten cua moi nguoi va them vao list name
print(name) # ['Elsa', 'Anna', 'Olaf']    

#Phase 4: pandas, DataFrame
import pandas as pd
df = pd.DataFrame(gpa, columns=["Name", "Age", "GPA"]) # tao 1 DataFrame tu list gpa, dat ten cot la Name, Age, GPA
print(df) #     Name  Age  GPA
          #0   Elsa   21  3.5   

#Phase 5: Matrix, List Comprehension
#matrix, list comprehension
matrix=[[1, 2, 3],
        [4, 5, 6],[7, 8, 9]]
tranpose = [[row[i] for row in matrix] for i in range(3)]  #list comprehension 
print(tranpose) #[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Nested loops, lists 2D
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for row in matrix:
    for number in row:
        print(number, end=" ")
    print()  #1 2 3
             #4 5 6 
             #7 8 9
#EXERCISES
#1
#1.1
scores = [85, 92, 78, 90, 88, 76, 95, 83]

# 1. Phần tử đầu và cuối
print(scores[0])   # 85
print(scores[-1])  # 83

# 2. 3 phần tử đầu
print(scores[:3])  # [85, 92, 78]

# 3. 3 phần tử cuối
print(scores[-3:]) # [76, 95, 83]

# 4. Phần tử index 4
print(scores[4])   # 88

#1.2
students = []

# 1. Thêm 5 tên
students.append("An")
students.append("Binh")
students.append("Chi")
students.append("Dung")
students.append("Em")
print(students)  # ['An', 'Binh', 'Chi', 'Dung', 'Em']

# 2. Xóa tên đầu tiên
students.pop(0)
print(students)  # ['Binh', 'Chi', 'Dung', 'Em']

# 3. Chèn vào index 2
students.insert(2, "Phong")
print(students)  # ['Binh', 'Chi', 'Phong', 'Dung', 'Em']

#1.3
fruits = ["apple", "banana", "mango", "apple", "orange", "banana", "apple"]

# 1. Đếm số lần xuất hiện
print(fruits.count("apple"))   # 3

# 2. Tìm index
print(fruits.index("mango"))   # 2

# 3. Kiểm tra tồn tại
print("grape" in fruits)       # False

#2
#2.1
numbers = [4, 17, 3, 25, 8, 42, 11, 6, 33, 19]

# 1. Số chẵn
for n in numbers:
    if n % 2 == 0:
        print(n)   # 4, 8, 42, 6

# 2. Số lớn hơn 15
for n in numbers:
    if n > 15:
        print(n)   # 17, 25, 42, 33, 19

# 3. Tính tổng KHÔNG dùng sum()
total = 0
for n in numbers:
    total += n
print(total)       # 168

# 4. Tìm max KHÔNG dùng max()
biggest = numbers[0]          # Giả sử phần tử đầu là lớn nhất
for n in numbers:
    if n > biggest:
        biggest = n           # Cập nhật nếu tìm thấy số lớn hơn
print(biggest)     # 42

#2.2 LIST COMPREHENSION
temps_celsius = [0, 15, 22, 30, 37, -5, 100]

# 1. Chuyển sang Fahrenheit
temps_f = [c * 9/5 + 32 for c in temps_celsius]
print(temps_f)
# [32.0, 59.0, 71.6, 86.0, 98.6, 23.0, 212.0]

# 2. Lọc nhiệt độ > 20
hot = [c for c in temps_celsius if c > 20]
print(hot)         # [22, 30, 37, 100]

# 3. Tạo chuỗi có ký hiệu °C
labels = [f"{c}°C" for c in temps_celsius]
print(labels)
# ['0°C', '15°C', '22°C', '30°C', '37°C', '-5°C', '100°C']

#2.3 ORGANIZE, REVERSE
names = ["Charlie", "Alice", "Eve", "Bob", "Diana"]

# 1. A → Z
print(sorted(names))
# ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

# 2. Z → A
print(sorted(names, reverse=True))
# ['Eve', 'Diana', 'Charlie', 'Bob', 'Alice']

# 3. Theo độ dài tên
print(sorted(names, key=len))
# ['Eve', 'Bob', 'Alice', 'Diana', 'Charlie']

# 4. Đảo ngược list gốc
print(names[::-1])
# ['Diana', 'Bob', 'Eve', 'Alice', 'Charlie']

#3 AVANCED
#3.1 Analysis score
grades = [72, 88, 95, 61, 79, 88, 92, 55, 83, 77]

# 1. Điểm trung bình
mean = sum(grades) / len(grades)
print(f"Trung bình: {mean}")         # 79.0

# 2. Cao nhất, thấp nhất
print(f"Cao nhất: {max(grades)}")    # 95
print(f"Thấp nhất: {min(grades)}")   # 55

# 3. Số học sinh đạt >= 80
count_80 = len([g for g in grades if g >= 80])
print(f"Số HS >= 80: {count_80}")    # 4

# 4. Xếp loại
def xep_loai(diem):
    if diem >= 90:
        return "Xuất sắc"
    elif diem >= 80:
        return "Giỏi"
    elif diem >= 70:
        return "Khá"
    elif diem >= 60:
        return "Trung bình"
    else:
        return "Yếu"

ket_qua = [xep_loai(g) for g in grades]
print(ket_qua)
# ['Khá', 'Giỏi', 'Xuất sắc', 'Trung bình', 'Khá',
#  'Giỏi', 'Xuất sắc', 'Yếu', 'Giỏi', 'Khá']grades = [72, 88, 95, 61, 79, 88, 92, 55, 83, 77]

#3.2 Data Cleaning
raw_data = [12, None, 7, -999, 25, None, 18, -999, 30, 5]

# 1. Lọc ra data sạch
clean = [x for x in raw_data if x is not None and x != -999]
print(clean)   # [12, 7, 25, 18, 30, 5]

# 2. Tính mean của data sạch
mean = sum(clean) / len(clean)
print(f"Mean: {mean}")   # 16.17

# 3. Thay None bằng mean (imputation)
#    Giữ nguyên -999 vì đó là lỗi, chỉ xử lý None
imputed = [mean if x is None else x for x in raw_data]
print(imputed)
# [12, 16.17, 7, -999, 25, 16.17, 18, -999, 30, 5]  

#3.3 Analysis revenue
revenue = [120, 135, 98, 142, 167, 189, 201, 178, 155, 143, 168, 210]

# 1. Tổng doanh thu
total = sum(revenue)
print(f"Tổng: {total} triệu")              # 1906 triệu

# 2. Trung bình mỗi tháng
mean = total / len(revenue)
print(f"Trung bình: {mean:.1f} triệu")     # 158.8 triệu

# 3. Tháng có doanh thu cao nhất
max_val = max(revenue)
thang = revenue.index(max_val) + 1         # +1 vì index bắt đầu từ 0
print(f"Tháng cao nhất: Tháng {thang} ({max_val} triệu)")  # Tháng 12

# 4. Số tháng trên mức trung bình
tren_tb = len([r for r in revenue if r > mean])
print(f"Số tháng > trung bình: {tren_tb}") # 6

# 5. Tăng trưởng so tháng trước (MoM Growth)
growth = []
for i in range(1, len(revenue)):           # Bắt đầu từ index 1 (tháng 2)
    g = (revenue[i] - revenue[i-1]) / revenue[i-1] * 100
    growth.append(round(g, 1))

print("Tăng trưởng MoM (%):", growth)
# [12.5, -27.4, 44.9, 17.6, 13.2, 6.3, -11.4, -13.0, -7.7, 17.5, 25.0]

# 6. Doanh thu theo quý
quy = []

for i in range(0, 12, 3):                 # Bước nhảy 3: 0, 3, 6, 9
    tong_quy = sum(revenue[i:i+3])
    quy.append(tong_quy)

for i, q in enumerate(quy):
    print(f"Quý {i+1}: {q} triệu")
# Quý 1: 353  |  Quý 2: 498  |  Quý 3: 534  |  Quý 4: 521

#______________________________________________________________________________________________________________________________________
# DICTIONARY
s_list = [ "Alice", 22, 8.5] # KO RO PHAN TU NAO TUONG UNG GI
s_dict = {"name": "Alice",
           "age": 22,
           "gpa": 8.5} # RO RANG PHAN TU NAO TUONG UNG GI
print(s_dict["name"]) # Alice
print(s_dict["age"])  # 22     
name
#get method
print(s_dict.get(""))          # Alice
print(s_dict.get("major", "Unknown")) # Unknown, tra ve gia tri mac dinh neu key khong ton tai 

#Apply, change, delete
s_dict["age"]= 23   # thay doi gia tri cua key age
s_dict["Major"]= "Computer Science"  # them key Major vao dict, gia tri la Computer Science
del s_dict["gpa"] # xoa key gpa khoi dict
age = s_dict.pop("age") # xoa key age va tra ve gia tri cua age
print(age) # 23

print("Major" in s_dict) # True, kiem tra xem key Major co ton tai trong dict hay khong
print("gpa" in s_dict)   # False, key gpa da bi xoa 

#Duyet dict
for key in s_dict.keys():  #KEYS
    print(key) # name, Major

for value in s_dict.values(): #VALUES
    print(value) # Alice, Computer Science

for key,value in s_dict.items():  #ITEMS, duyet qua tung cap key-value trong dict
    print(f"{key}:{value}") # name: Alice, Major: Computer Science

#LIST OF DICTIONARIES
data = [
    {"name":"Alice","age":22,"salary":55000},
    {"name":"Bob","age":24,"salary":70000},   # 2 dict trong list, moi dict chua thong tin cua 1 nguoi, cac key la name, age, salary
    {"name":"Carol","age":35,"salary":80000}
]

print(data[0]["salary"]) # 55000, lay salary cua nguoi dau tien trong list data
print(data[1]["age"]) # 24, lay age cua nguoi thu 2 trong list data
print(data[2]["name"]) # Carol, lay name cua nguoi thu 3 trong list data

people =[d["name"]for d in data]
print(people)
# ['Alice', 'Bob', 'Carol'], list comprehension, duyet qua tung dict trong list data, lay name cua moi nguoi va them vao list people

result = [d["name"] for d in data if d["salary"] > 60000] 
# List comprehension, duyet qua tung dict trong list data, neu salary > 60000 thi lay name va them vao list result
print(result) # ['Bob', 'Carol']

import pandas as pd
df = pd.DataFrame(data, columns =["name", "age", "salary"])
# tao 1 DataFrame tu list data, dat ten cot la name, age, salary
print(df) #    name  age  salary
          #0  Alice   22   55000    
          #1    Bob   24   70000
          #2  Carol   35   80000

# DICTIONARY COMPREHENSION
names = ["Alice", "Bob", "Charlie"]
ages = [22, 24, 35]
name_age = {name: age for name, age in zip(names, ages)} # Dictionary comprehension, zip 2 list names va ages lai voi nhau, tao dict name_age voi key la name va value la age
print(name_age) # {'Alice': 22, 'Bob': 24, 'Charlie': 35}

#EXERCISES
#1.
gpa ={
    "Ten sinh vien":"Minh",
    "Math": 8.5,
    "Physics": 7.0,
    "Chemistry": 9.0
}
print(gpa["Ten sinh vien"])# Minh
gpa["Literature"] = 6.5 # them key Literature vao dict gpa, gia tri la 6.5
gpa["Math"] = 9.0
del gpa["Physics"] # xoa key Physics khoi dict gpa
print(gpa)# {'Ten sinh vien': 'Minh', 'Math': 9.0, 'Chemistry': 9.0, 'Literature': 6.5}

#2
scores = {
    "Alice": 85,
    "Bob": 92,
    "Carol": 78,
    "David": 95,
    "Eve": 60
}
for name, score in scores.items():
    print(f"{name}:{score}")
# Alice:85 Bob:92 Carol:78 David:95 Eve:60

avg = sum(scores.values())/len(scores)
print(f" Average score: {avg}") # Average score: 82.0

top_student = max(scores, key = lambda x: scores[x])
print(f"Top student: {top_student} with score {scores[top_student]}") # Top student: David with score 95

#3
employees = {
    "E001": {"name": "Nguyen Van A", "dept": "Data", "salary": 15000000},
    "E002": {"name": "Tran Thi B",  "dept": "AI",   "salary": 18000000},
    "E003": {"name": "Le Van C",    "dept": "Data", "salary": 12000000},
    "E004": {"name": "Pham Thi D",  "dept": "AI",   "salary": 20000000},
}

#  In tên nhân viên E002
print(employees["E002"]["name"])
# Truy cập 2 lớp: dict ngoài["E002"] → dict trong["name"]
# Output: Tran Thi B

#  Tăng lương phòng Data lên 10%
for info in employees.values():
    if info["dept"] == "Data":
        info["salary"] = info["salary"] * 1.1
        # Nhân 1.1 = tăng thêm 10%
        # Vì info là dict (object), sửa trực tiếp sẽ thay đổi luôn trong employees

#  Danh sách tên phòng AI
ai_employees = [info["name"] for info in employees.values()
                if info["dept"] == "AI"]
# List comprehension: lọc những người có dept == "AI", lấy ra tên
print(ai_employees)
# ['Tran Thi B', 'Pham Thi D']

#  Tổng quỹ lương
total_salary = sum(info["salary"] for info in employees.values())
# employees.values() → từng dict con
# lấy ["salary"] từ mỗi dict → cộng tất cả lại
print(f"Tổng quỹ lương: {total_salary:,.0f} VNĐ")
# Output: 68,500,000 VNĐ  (Data đã được tăng 10%)

#4
raw_data = [
    ("apple", 3),
    ("banana", 5),
    ("cherry", 1),
    ("date", 8),
    ("elderberry", 2)
]

#  Tạo dict từ list
fruit_dict = {k: v for k, v in raw_data}
# Với mỗi tuple (k, v) trong raw_data → tạo cặp key:value
print(fruit_dict)
# {'apple': 3, 'banana': 5, 'cherry': 1, 'date': 8, 'elderberry': 2}

#  Chỉ giữ item có value > 3
filtered = {k: v for k, v in raw_data if v > 3}
# Thêm điều kiện "if" vào cuối comprehension để lọc
print(filtered)
# {'banana': 5, 'date': 8}

#  Nhân đôi value
doubled = {k: v * 2 for k, v in raw_data}
# Thay đổi phần VALUE (v*2) trong comprehension
print(doubled)
# {'apple': 6, 'banana': 10, 'cherry': 2, 'date': 16, 'elderberry': 4}

#       {key_expr : value_expr   for k, v in iterable          if condition}
 #         Tạo key và value         Nguồn dữ liệu          Điều kiện lọc (tuỳ chọn)

#5
transactions = [
    {"id": 1, "category": "Food",          "amount": 150000},
    {"id": 2, "category": "Transport",     "amount": 50000},
    {"id": 3, "category": "Food",          "amount": 200000},
    {"id": 4, "category": "Entertainment", "amount": 300000},
    {"id": 5, "category": "Transport",     "amount": 80000},
    {"id": 6, "category": "Food",          "amount": 120000},
    {"id": 7, "category": "Entertainment", "amount": 150000},
]

#  Tổng chi tiêu theo category
spending_by_category = {}

for t in transactions:
    cat = t["category"]
    amt = t["amount"]
    
    if cat not in spending_by_category:
        spending_by_category[cat] = 0      # Lần đầu gặp category → khởi tạo = 0
    
    spending_by_category[cat] += amt       # Cộng dồn vào

print(spending_by_category)
# {'Food': 470000, 'Transport': 130000, 'Entertainment': 450000}

#  Category tốn tiền nhất
top_category = max(spending_by_category, key=lambda x: spending_by_category[x])
print(f"Tốn tiền nhất: {top_category}")   # Food

#  Phần trăm từng category
total = sum(spending_by_category.values())

percentage = {
    cat: round(amt / total * 100, 2)
    for cat, amt in spending_by_category.items()
}
print(percentage)
# {'Food': 44.76, 'Transport': 12.38, 'Entertainment': 42.86}

#  BONUS — In báo cáo đẹp
# Sắp xếp theo chi tiêu giảm dần
sorted_spending = dict(
    sorted(spending_by_category.items(), key=lambda x: x[1], reverse=True)
)

print("BÁO CÁO CHI TIÊU")
print("=" * 30) 

for cat, amt in sorted_spending.items():
    pct = round(amt / total * 100, 2)
print(f"{cat:<15}: {amt:>10,.0f} VNĐ ({pct}%)")
    # {cat:<15}  → căn trái, chiếm 15 ký tự
    # {amt:>10,.0f} → căn phải, có dấu phẩy phân cách nghìn, không thập phân

print("=" * 30)
print(f"{'Tổng cộng':<15}: {total:>10,.0f} VNĐ")

#NUMPY

#old, slow
diem=[6,7,8,5,9]
diem_bonus=[d +5 for d in diem]
print(diem_bonus)
#[11,12,13,10,14]

#use numpy
import numpy as np
diem = np.array([6,7,8,5,9])
diem+=5
print(diem)
#[11,12,13,10,14]
 
#1D
revenue = np.array([120, 250, 310, 180, 400])
print(revenue) #120, 250, 310, 180, 400
print(revenue.shape)#5      5 phan tu/1 chieu
print(revenue.dtype)   #type int

#2D like excel table
workers_revenue = np.array([
    [120, 150, 200, 180],   #worker A
    [200, 220, 190, 210],   #worker B        #Mỗi hàng = 1 nv, mỗi cột = doanh thu theo quý
    [95, 110, 130, 120]     #worker C
])

print(workers_revenue.shape)  #(3, 4)   3 hang 4 cot
print(workers_revenue.ndim)   #2   2 dimensions
print(workers_revenue.size)   #12  12 phan tu

# Cac cach tao array nhanh
results = np.zeros(5)
print(result)  #[0, 0, 0, 0, 0]
#Dùng khi: khởi tạo mảng kết quả trước khi tính

prices = np.ones(4)*50000
print(prices)    #[50000, 50000, 50000, 50000]
#Tất cả giá đều là 50000


#np.arange, tạo dãy số(giống range() nhưng ra array)
#syntax: np.arane(start, stop, step)
days = np.arange(1, 8) #1,2,3,4,5,6,7
print(days)
small_cut = np.arange(0, 1, 0.1)
print(small_cut)  # 0, 0.1...0.9

#linspace
x = np.linspace(0, 100, 5)
print(x) #[  0.  25.  50.  75. 100.]
#Dùng khi: vẽ đồ thị, chia khoảng cách đều nhau 

#np.random.rand, tạo số ngẫu nhiên từ 0 đến 1
#Dùng khi: tạo dữ liệu giả để test

model_test = np.random.rand(3)
print(model_test) #[0.08474927 0.7488159  0.04197393]

#3x3 matrix
matrix = np.random.rand(3, 3)
print(matrix)
#[[0.79513994 0.55924581 0.13897204]
#[0.58645947 0.70041849 0.44395167]
#[0.9716037  0.71097047 0.38164827]]

# ✏️  Tóm tắt 1 dòng: array() tạo từ dữ liệu có sẵn;
#     zeros/ones/arange/linspace tạo dữ liệu mẫu.

# 1.3 Indexing & Slicing (Truy cập dữ liệu)
# -----------------------------------------------------------------------------

# --- Mảng 1D — giống list Python ---

diem_thi = np.array([6.5, 7.0, 8.5, 5.0, 9.0, 7.5])
#  index:              0    1    2    3    4    5
#  index âm:          -6   -5   -4   -3   -2   -1

# Lấy 1 phần tử
print(diem_thi[0])    # 6.5  (phần tử đầu tiên)
print(diem_thi[-1])   # 7.5  (phần tử cuối cùng)

# Slicing: [start : stop : step]   (stop KHÔNG bao gồm)
print(diem_thi[1:4])  # [7.  8.5 5. ]  → index 1, 2, 3
print(diem_thi[:3])   # [6.5 7.  8.5]  → 3 phần tử đầu
print(diem_thi[3:])   # [5.  9.  7.5]  → từ index 3 đến hết
print(diem_thi[::2])  # [6.5 8.5 9. ]  → mỗi 2 phần tử lấy 1

# --- Mảng 2D — dùng [hàng, cột] ---

# Bảng điểm: 4 học sinh, 3 môn (Toán, Lý, Hóa)
bang_diem = np.array([
    [8.0, 7.5, 9.0],   # HS 1
    [6.5, 8.0, 7.0],   # HS 2
    [9.0, 9.5, 8.5],   # HS 3
    [5.5, 6.0, 7.5],   # HS 4
])
#  cột:  0    1    2

# Lấy 1 ô: [hàng, cột]
print(bang_diem[0, 0])   # 8.0  → HS 1, môn Toán
print(bang_diem[2, 1])   # 9.5  → HS 3, môn Lý
print(bang_diem[-1, -1]) # 7.5  → HS cuối, môn cuối

# Lấy cả 1 hàng (1 học sinh)
print(bang_diem[1])      # [6.5 8.  7. ]  → tất cả điểm HS 2
print(bang_diem[1, :])   # [6.5 8.  7. ]  → cách viết rõ hơn

# Lấy cả 1 cột (1 môn học)
print(bang_diem[:, 0])   # [8.  6.5 9.  5.5] → điểm Toán tất cả HS
print(bang_diem[:, 1])   # [7.5 8.  9.5 6. ]  → điểm Lý tất cả HS

# Lấy một vùng (submatrix)
print(bang_diem[0:2, 1:3])
# [[7.5 9. ]   → HS 1, 2 môn cuối
#  [8.  7. ]]  → HS 2, 2 môn cuối


# --- Boolean Indexing — lọc theo điều kiện ---

diem_thi = np.array([6.5, 7.0, 8.5, 5.0, 9.0, 4.5])
ten_hs   = np.array(["An", "Bình", "Chi", "Duy", "Em", "Phúc"])

# Bước 1: Tạo mảng True/False
dk_dat = diem_thi >= 5.0
print(dk_dat)   # [ True  True  True  True  True False]

# Bước 2: Dùng điều kiện để lọc
diem_dat = diem_thi[dk_dat]
print(diem_dat)  # [6.5 7.  8.5 5.  9. ]

# Viết gọn lại (cách thông dụng nhất):
hs_truot = ten_hs[diem_thi < 5.0]
print(hs_truot)  # ['Phúc']

hs_gioi  = ten_hs[diem_thi >= 8.0]
print(hs_gioi)   # ['Chi' 'Em']

# Kết hợp nhiều điều kiện: dùng & (and), | (or)
# ⚠️  PHẢI có ngoặc () quanh mỗi điều kiện
diem_tb_kha = diem_thi[(diem_thi >= 6.5) & (diem_thi < 8.0)]
print(diem_tb_kha)  # [6.5 7. ]

# ✏️  Tóm tắt 1 dòng: array[điều kiện] trả về tất cả phần tử thỏa điều kiện.



# --- Vectorized Operations (Tính từng phần tử) ---

# Dữ liệu bán hàng: giá và số lượng từng sản phẩm
gia    = np.array([150000, 80000, 250000, 120000])  # đồng
sl     = np.array([10,     25,    5,      15])       # cái

# ✅ NumPy tự nhân từng cặp (không cần vòng lặp)
doanh_thu = gia * sl
print(doanh_thu)  # [1500000 2000000 1250000 1800000]

# Tính giảm giá 10%
gia_giam = gia * 0.9
print(gia_giam)   # [135000.  72000. 225000. 108000.]

# Cộng, trừ, chia đều hoạt động tương tự
phi_ship = np.array([10000, 10000, 15000, 10000])
tong_tien = doanh_thu + phi_ship
print(tong_tien)  # [1510000 2010000 1265000 1810000]

# --- Các hàm thống kê quan trọng ---

diem = np.array([7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 5.5, 9.5])

print(np.sum(diem))     # 61.5   → tổng
print(np.mean(diem))    # 7.6875 → trung bình
print(np.median(diem))  # 7.75   → trung vị (phần tử giữa khi sắp xếp)
print(np.std(diem))     # 1.2... → độ lệch chuẩn (data phân tán thế nào)
print(np.var(diem))     # 1.4... → phương sai

print(np.min(diem))     # 5.5    → nhỏ nhất
print(np.max(diem))     # 9.5    → lớn nhất
print(np.argmin(diem))  # 6      → INDEX của phần tử nhỏ nhất
print(np.argmax(diem))  # 7      → INDEX của phần tử lớn nhất

# Sắp xếp
print(np.sort(diem))    # [5.5 6.5 7.  7.5 8.  8.5 9.  9.5]

# Phần trăm (percentile) — rất hay dùng trong EDA
print(np.percentile(diem, 25))  # 7.0  → Q1: 25% học sinh dưới điểm này
print(np.percentile(diem, 50))  # 7.75 → Q2: trung vị
print(np.percentile(diem, 75))  # 8.5  → Q3: 75% học sinh dưới điểm này


# --- Tính theo trục (axis) trong mảng 2D ---

# Bảng doanh thu: 3 nhân viên, 4 tháng
doanh_thu = np.array([
    [120, 150, 200, 180],   # NV A
    [200, 220, 190, 210],   # NV B
    [95,  110, 130, 120],   # NV C
])

# axis=0 → tính theo chiều DỌC (gộp các hàng lại)
# → kết quả: 1 giá trị cho mỗi CỘT (mỗi tháng)
trung_binh_thang = np.mean(doanh_thu, axis=0)
print(trung_binh_thang)
# [138.33 160.   173.33 170.  ] → TB mỗi tháng của toàn bộ NV

# axis=1 → tính theo chiều NGANG (gộp các cột lại)
# → kết quả: 1 giá trị cho mỗi HÀNG (mỗi nhân viên)
tong_NV = np.sum(doanh_thu, axis=1)
print(tong_NV)
# [650 820 455] → tổng doanh thu của từng NV

# ✏️  Nhớ mẹo axis:
#     axis=0 → "xuyên qua các hàng" (kết quả theo cột)
#     axis=1 → "xuyên qua các cột" (kết quả theo hàng)

# -----------------------------------------------------------------------------
# 1.5 Reshape & Transpose
# -----------------------------------------------------------------------------

# reshape: đổi hình dạng mảng, KHÔNG thay đổi dữ liệu
data = np.arange(12)           # [0 1 2 3 4 5 6 7 8 9 10 11]
print(data.shape)              # (12,)

bang = data.reshape(3, 4)      # 3 hàng, 4 cột (3×4 = 12 ✅)
print(bang)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Dùng -1: NumPy tự tính chiều đó
bang2 = data.reshape(4, -1)    # 4 hàng, NumPy tính ra 3 cột
print(bang2.shape)             # (4, 3)

# flatten: chuyển mảng nhiều chiều về 1 chiều
flat = bang.flatten()
print(flat)   # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# Transpose: đổi hàng thành cột (xoay 90°)
ma_tran = np.array([[1, 2, 3],
                    [4, 5, 6]])
print(ma_tran.shape)        # (2, 3)
print(ma_tran.T.shape)      # (3, 2)
print(ma_tran.T)
# [[1 4]
#  [2 5]
#  [3 6]]

#EXCERCISES

#1 Normalize
diem = np.array([4.5, 6.0, 7.5, 8.0, 9.5, 5.0, 7.0])
diem_chuan_hoa = (diem-diem.min())/(diem.max()-diem.min())
print(diem_chuan_hoa)

#2 Boolean Masking, NaN
nhiet_do = np.array([28.0, 72.0, 31.5, -5.0, 29.0, 41.0, 25.5])
nhiet_do[(nhiet_do<10)|(nhiet_do>40)] = np.nan
print(nhiet_do)

#3 Ma trận đường chéo
gia_tri = np.array([1, 2, 3, 4, 5])
matrix = np.diag(gia_tri)
print(matrix)

#4 Broadcasting, Khoảng cách Euclidean, newaxis
diem = np.array([[0,0], [1,0], [0,1], [1,1]], dtype=float)
diff = diem[:, np.newaxis :] - diem[np.newaxis, :, :]
ds_matrix = np.sqrt((diff**2).sum(axis=2))


#5 Boolean Masking
diem   = np.array([7.0, 8.5, 6.0, 9.0, 5.5, 7.5, 8.0, 6.5])
nhom   = np.array([ 'A',  'B',  'A',  'B',  'A',  'B',  'A',  'B'])

tb_A = diem[nhom=="A"].mean()
tb_b = diem[nhom=="B"].mean()

#B1
diem = np.array([4.0, 7.5, 3.5, 8.0, 5.0, 6.5, 2.5, 9.0, 4.5, 7.0])
diem_dat =  diem[diem>=5]
so_dat = len(diem_dat)
so_dat = (diem>5).sum()
tb_dat = diem_dat.mean()

tb_truot = diem[diem<5].mean()

print(so_dat)
print(tb_dat)
print(tb_truot)

#B2
diem = np.array([6,8,7, 5,9,8, 7,6,9, 8,10,9])
print(diem.reshape(4,3))
mean_each_week = np.mean(diem.reshape(4,3), axis =1)
print(mean_each_week)

diem = np.array([6,8,7, 5,9,8, 7,6,9, 8,10,9])
col_mean = np.mean(diem.reshape(4,3), axis =0)
col_std = np.std(diem.reshape(4,3), axis =0)           # std = Standard Devitation (Độ lệch chuẩn)
Z_score = (diem.reshape(4,3) - col_mean)/col_std       # để đo sự phân tán data
print(col_mean)                                        # Độ lệch chuẩn so với trung bình
print(col_std)
print(Z_score)


# =============================================================================
# PHẦN 2: PANDAS
# =============================================================================
# 2.1 Tại sao cần Pandas
# Pandas giải quyết giới hạn của NumPy:
# - NumPy chỉ chứa một kiểu dữ liệu (toàn số hoặc toàn string)
# - NumPy không có tên cột/hàng → khó đọc
# - NumPy không xử lý được dữ liệu thiếu (NaN)
# - NumPy không đọc được file CSV, Excel
# Pandas là thư viện số 1 của Data Science — bạn sẽ dùng nó HÀNG NGÀY.


# -----------------------------------------------------------------------------
# 2.2 Series — Mảng 1 chiều có nhãn
# -----------------------------------------------------------------------------

import pandas as pd
diem_toan = pd.Series([8.0, 7.0, 9.0, 6.5, 8.5])
print(diem_toan)  #tự động đánh index
#0    8.0
#1    7.5
#2    9.0
#3    6.5
#4    8.5
#dtype: float64

#Tạo Series với index tự đặt
diem_anh = pd.Series([8.5, 9.0, 7.3, 8.0, 9.5],
                     index = ["An", "Bình", "Chi", "Duy", "Em"])
#An      8.5
#Bình    9.0
#Chi     7.3
#Duy     8.0
#Em      9.5
print(diem_anh)


#Tạo từ Dict-key tự động thành index
chi_tieu = pd.Series({
    "Food":      2500000,
    "Rent":      3000000,
    "Transport": 500000,
    "Entertain": 800000
})

print(chi_tieu)

#Food         2500000
#Rent         3000000
#Transport     500000
#Entertain     800000
#dtype: int64

#Truy cap bang label
print(chi_tieu["Food"])
print(chi_tieu["Entertain"])

#Truy cap bang vi tri so

print(chi_tieu.iloc[0])
print(chi_tieu.iloc[2])

#Slicing
print(chi_tieu["Food":"Transport"])  #kèm điểm dừng
print(chi_tieu.iloc[0:2])            #không kèm điểm dừng

#Boolean indexing
expense = chi_tieu[chi_tieu>1000000]  #Lọc theo điều kiện
print(f"Expense:{expense}")

cheap = chi_tieu[chi_tieu<1000000]
print(f"Cheap:{cheap}")

#Calculate in Series
print(chi_tieu.sum())
print(chi_tieu.mean())
print(chi_tieu.max())
print(chi_tieu.min())

#idxmax / idxmin -> trả về tên, không phải giá trị
print(chi_tieu.idxmax())
print(chi_tieu.idxmin())

print(chi_tieu.argmax())
print(chi_tieu.argmin())

pct = chi_tieu / chi_tieu.sum()*100
print(f"Percentage per category: {pct.round(1)}")

#Summary: Series = cột dữ liệu có tên hàng(index), có thể tính toán, lọc như Numpy


# -----------------------------------------------------------------------------
# 2.3 DataFrame — Trái tim của Pandas
# -----------------------------------------------------------------------------


# DataFrame = bảng dữ liệu 2 chiều, giống Excel.
# Mỗi cột là một Series, tất cả dùng chung index (tên hàng)

# Tạo DataFrame từ dictionary
# Key = tên cột, Value = danh sách dữ liệu của cột đó

nhan_vien = pd.DataFrame({
    "Ten":       ["An",    "Bình",  "Chi",   "Duy",   "Em"],
    "Phong":     ["IT",    "Kinh doanh", "IT", "HR", "Kinh doanh"],
    "Luong":     [15000000, 20000000, 18000000, 12000000, 22000000],
    "KinhNghiem": [3,       5,        4,        2,        6]
})
print(nhan_vien)

#    Ten       Phong     Luong  KinhNghiem
#0    An          IT  15000000           3
#1  Bình  Kinh doanh  20000000           5
#2   Chi          IT  18000000           4
#3   Duy          HR  12000000           2
#4    Em  Kinh doanh  22000000           6


#Explore Dataframe (EDA)
#Always do these things first

print(nhan_vien.shape)      #(5,4) 5 hàng 4 cột
print(nhan_vien.dtypes)     # data types
print(nhan_vien.info())     #data types, non-null
print(nhan_vien.describe()) # Thống kê nhanh

print(nhan_vien.head(3))  # 3 hàng đầu
print(nhan_vien.tail(2))  # 2 hàng cuối


# Truy cập cột và hàng

#CỘT

luong = nhan_vien["Luong"]
print(luong)        #Lấy một cột, trả về Series
print(type(luong))  # Data types


#Lấy nhiều cột, trả về DataFrame
info = nhan_vien[["Ten", "Luong"]]
print(info)
#    Ten     Luong
#0    An  15000000
#1  Bình  20000000
#2   Chi  18000000
#3   Duy  12000000
#4    Em  22000000

#HÀNG
#.loc()  truy cập bằng tên index
print(nhan_vien.loc[0])   # Hàng đầu tiên
print(nhan_vien.loc[2])   # Hàng thứ 3

#.iloc() truy cập bằng vị trí số
print(nhan_vien.iloc(0))
print(nhan_vien.iloc[0:2])
print(nhan_vien.iloc[-1])


# -----------------------------------------------------------------------------
# 2.4 Đọc Dữ Liệu Thực Tế
# -----------------------------------------------------------------------------

# Đọc file CSV (phổ biến nhất)
#df = pd.read_csv("data/sales.csv")

# Các tham số hay dùng:
#df = pd.read_csv(
#   "data/sales.csv",     
#     sep=",",                 #dấu phân cách, mặc định là dấu phẩy      
#     encoding="utf-8",       # mã hóa ký tự (utf-8-sig cho file tiếng Việt)
#     index_col=0,            # cột nào làm index (thường dùng cột ID)
#     parse_dates=["NgayBan"] # chuyển cột này sang kiểu datetime tự động
# )

# Đọc file Excel
#df = pd.read_excel("data/bao_cao.xlsx", sheet_name="Sheet1")

# Lưu file CSV
#df.to_csv("output/ket_qua.csv", index=False)  # index=False: không lưu index_col
#df.to_csv("output/ket_qua.csv", index = True) #index = True: lưu index_col



# -----------------------------------------------------------------------------
# 2.5 Sampling — Lấy Mẫu Dữ Liệu
# -------------------------------------;''----------------------------------------

# Harvard CS109 nhấn mạnh: cách bạn lấy mẫu ảnh hưởng trực tiếp đến kết luận.
# Dataset lớn không phải lúc nào cũng cần dùng hết — và lấy mẫu sai → bias.

# Giả sử có dataset 10,000 đơn hàng
np.random.seed(42)
df = pd.DataFrame({
    "OrderCode": range(1001),
    "Price": np.random.exponential(500000, 1001).round(),
    "Area":np.random.choice(["HCM", "HN", "DN", "CT"], 1001, p=[0.4, 0.35, 0.15, 0.1])
})

# --- Random Sampling: lấy mẫu ngẫu nhiên ---
# Dùng khi: dataset quá lớn, muốn test nhanh
ex200 = df.sample(n=200, random_state=42)       #lấy ngẫu nhiên 200 số
ex25pct = df.sample(frac=0.25, random_state=42) #lấy 25% random_state = random.seed()


# --- Stratified Sampling: lấy mẫu theo tỉ lệ nhóm ---
# Dùng khi: muốn mẫu đại diện cho TẤT CẢ nhóm
# Ví dụ: đảm bảo HCM/HN/DN/CT đều có trong mẫu theo đúng tỉ lệ
ex_stratified = df.groupby("Area", group_keys=False).sample(
    frac=0.25,
    random_state=42
)
print(ex_stratified)
print(ex_stratified["Area"].value_counts(normalize=True)*100)

# Tại sao Stratified quan trọng hơn Random?
# Nếu random sampling "xui" bỏ sót khu vực CT (chỉ có 10%),
# mọi kết luận về CT sẽ sai.
# Stratified đảm bảo mọi nhóm đều được đại diện.

# ✏️  Tóm tắt 1 dòng: Random = nhanh;
#     Stratified = chính xác hơn khi data có nhóm không đều nhau.


# -----------------------------------------------------------------------------
# 2.6 loc và iloc — Truy Cập Nâng Cao
# -----------------------------------------------------------------------------

orders = pd.DataFrame({
    "SanPham": ["Ao", "Quan", "Giay", "Tui", "Mu"],
    "GiaBan": [200, 350, 500, 450, 120],
    "SoLuong":[50, 30, 20, 15, 80],
    "DanhMuc":["Maymac", "Maymac", "Phukien", "Phukien", "Maymac"]
}, index =["DH001", "DH002", "DH003", "DH004", "DH005"])

print(orders)


# --- .loc → dùng NHÃN (label) ---
print(orders.loc["DH003"])
print(orders.loc["DH001":"DH003"])
print(orders.loc["DH004", "SoLuong"])
print(orders.loc[:,"GiaBan"])
print(orders.loc[:,["SanPham", "SoLuong"]])


# --- .iloc → dùng SỐ VỊ TRÍ (positon) ---
print(orders.iloc[2])
print(orders.iloc[0:3])
print(orders.iloc[2,1])
print(orders.iloc[:,2])
print(orders.iloc[1:3,0:2])

# Khi nào dùng loc, khi nào dùng iloc?
# ┌────────────────────────────────┬────────────────────────────────┐
# │ Tình huống                     │ Dùng                           │
# ├────────────────────────────────┼────────────────────────────────┤
# │ Biết tên hàng/cột              │ .loc["DH001", "GiaBan"]        │
# │ Biết vị trí số                 │ .iloc[0, 1]                    │
# │ Index là số bình thường (0,1…) │ Cả hai đều được                │
# │ Index là string (mã, tên…)     │ Bắt buộc dùng .loc             │
# │ Muốn lấy n hàng đầu/cuối      │ .iloc                          │
# └────────────────────────────────┴────────────────────────────────┘

# ✏️  Tóm tắt 1 dòng: loc = dùng TÊN; iloc = dùng SỐ.


# -----------------------------------------------------------------------------
# 2.7 Filtering — Lọc Dữ Liệu
# -----------------------------------------------------------------------------


# Đây là kỹ năng dùng HÀNG NGÀY trong Data Science.

nv = pd.DataFrame({
    "Ten":    ["An", "Bình", "Chi", "Duy", "Em", "Phúc"],
    "Phong":  ["IT", "KD",   "IT",  "HR",  "KD", "IT"],
    "Luong":  [15, 20, 18, 12, 22, 16],   # triệu
    "Nam":    [3,  5,  4,  2,  6,  1]     # năm kinh nghiệm
})

high_salary = nv[nv["Luong"]>17]
it = nv[nv["Phong"]=="IT"]


# Lọc nhiều điều kiện
# ⚠️  Dùng & (và), | (hoặc), ~ (phủ định) — KHÔNG dùng and/or
# ⚠️  PHẢI có ngoặc () quanh mỗi điều kiện

it_high_salary = nv[(nv["Phong"]=="IT")&(nv["Luong"]>15)]
kd_hr = nv[(nv["Phong"]=="KD")|(nv["Phong"]=="HR")]
not_it = nv[nv["Phong"]!="IT"]
not_it2 = nv[~(nv["Phong"]=="IT")]

# isin() → lọc nhiều giá trị cùng lúc
kd_hr2 = nv[nv["Phong"].isin(["KD", "HR"])]
it_high_salary2 = nv[nv["Phong"].eq("IT")& nv["Luong"].gt(15)]#eq = equal, gt = greater than


# between() → lọc khoảng giá trị
medium_salary = nv[nv["Luong"].between(15,20)]

# str.contains() → lọc theo chuỗi con (dùng cho cột text)
it_or_hr = nv[nv["Phong"].str.contains("IT|HR")]  # lọc những người làm IT hoặc HR

san_pham = pd.DataFrame({"Ten": ["Áo thun", "Áo khoác", "Quần jeans", "Áo polo"]})
Danhmuc_ao = san_pham[san_pham["Ten"].str.contains("Áo")]

# str.startswith() → lọc theo chuỗi bắt đầu
it_start = nv[nv["Phong"].str.startswith("IT")]

# str.endswith() → lọc theo chuỗi kết thúc
it_end = nv[nv["Phong"].str.endswith("IT") ]


# -----------------------------------------------------------------------------
# 2.8 Thêm, Sửa, Xóa Cột
# -----------------------------------------------------------------------------

nv = pd.DataFrame({
    "Ten":   ["An", "Bình", "Chi", "Duy"],
    "Luong": [15, 20, 18, 12],
    "Phong": ["IT", "KD", "IT", "HR"]
})
nv["Thue"] = nv["Luong"] * 0.1
nv["LuongSauThue"] = nv["Luong"] - nv["Thue"]
nv["CapBac"] = nv["Luong"].apply(lambda x : "Senior" if x >= 18 else "Junior")


# Sửa giá trị
nv["Phong"] = nv["Phong"].replace({"KD": "Kinh doanh", "HR": "Nhân sự"})  #Sửa cả cột theo mapping
nv.loc[nv["Ten"] == "An", "Luong"] = 17                                   #Sửa một ô duy nhất
nv.loc[nv["Ten"] == "Duy", ["Luong", "Phong"]] = [13, "Hành chính"]       #Sửa nhiều cột cùng lúc
nv.loc[nv["Luong"]>18, "CapBac"] = "Trưởng phòng"                         #Sửa theo điều kiện
nv.loc[nv["Luong"]==20, "Highest Salary"] = True                          #Thêm cột mới dựa trên điều kiện

print(nv)

# -----------------------------------------------------------------------------
# 2.9 Xử Lý Dữ Liệu Thiếu (Missing Data)
# -----------------------------------------------------------------------------
import pandas as pd
import numpy as np

# Dataset có missing values (NaN = Not a Number)
dfnan = pd.DataFrame({
    "Ten":    ["An", "Bình", None,   "Duy",    "Em"],
    "Tuoi":   [25,    np.nan, 28,    30,        np.nan],
    "Luong":  [15000, 20000,  18000, np.nan,    22000],
    "Kinh":   [3,     5,      4,     2,         6]
})
print(dfnan)

#Phát hiện Missing Data
print(dfnan.isnull())                       #  True = bị thiếu
print(dfnan.isnull().sum())                 # Đếm số Nan mỗi cột
print(dfnan.isnull().sum() / len(dfnan))    # Tính phần trăm Nan

# Xóa hàng có NaN
print(dfnan.dropna())                             # Xóa bất kì hàng nào có 
print(dfnan.dropna(subset = ["Luong", "Tuoi"]))   # Xóa hàng có cột lương và tuổi bị Nan
print(dfnan.dropna(thresh = 3))                   # Giữ hàng có ít nhất 3 giá trị ko Nan

# Điền giá trị vào chỗ thiếu
dfnan["Ten"] = dfnan["Ten"].fillna("Không rõ")

mean_luong = dfnan["Luong"].mean()   # điền bằng trung bình
dfnan["Luong"] = dfnan["Luong"].fillna(mean_luong)  

median_luong = dfnan["Luong"].median()# điền bằng trung vị ( tốt hơn nếu có outliers)
dfnan["Luong"] = dfnan["Luong"].fillna(median_luong)
dfnan["Luong"] = dfnan["Luong"].fillna(dfnan["Luong"].mean())

dfnan["Luong"] = dfnan["Luong"].ffill()  # forward fill
dfnan["Luong"] = dfnan["Luong"].bfill()  # backward fill
# tốt cho dữ liệu chuỗi thới gian


# Quy tắc chọn cách xử lý NaN:
# - Ít dữ liệu thiếu (<5%)      → dropna()
# - Nhiều thiếu, cột số         → fillna(mean) hoặc fillna(median)
# - Chuỗi thời gian             → fillna(method="ffill")
# - Cột text                    → fillna("Unknown")



# -----------------------------------------------------------------------------
# 2.10 GroupBy — Nhóm và Tổng Hợp
# -----------------------------------------------------------------------------

# GroupBy là tính năng MẠNH NHẤT của Pandas.
# Tư duy: "Tính X cho mỗi nhóm Y"


wk = pd.DataFrame({
    "Ten":   ["An", "Bình", "Chi", "Duy", "Em", "Phúc", "Giang"],
    "Phong": ["IT", "KD",   "IT",  "HR",  "KD", "IT",   "HR"],
    "Luong": [15,   20,     18,    12,    22,   16,     14],
    "Nam":   [3,    5,      4,     2,     6,    1,      3]
}).reset_index()

print(wk)

# GroupBy cơ bản: "Tính trung bình lương theo từng phòng"
mean_salary = wk.groupby("Phong")["Luong"].mean()
print(mean_salary)


# Nhiều hàm tổng hợp cùng lúc
tonghop = wk.groupby("Phong")["Luong"].agg(["mean","sum", "min", "max"])
print(tonghop)


room_df = wk.groupby("Phong")["Luong"].mean().reset_index()
print(f"room df:{room_df}")
 

# reset_index: chuyển kết quả GroupBy thành DataFrame bình thường

# GroupBy theo nhiều cột

df2 = pd.DataFrame({
    "Thang":[1,1,2,2,1,2],
    "SP": ["A","B","A","B","A","B"],
    "Doanh": [100,200,150,180,120,220]
})

tong_thang_sp = df2.groupby(["Thang","SP"])["Doanh"].sum().reset_index()
print(tong_thang_sp)

# ✏️  Tóm tắt 1 dòng: groupby("cột")["cột_khác"].hàm() = tính hàm đó cho từng nhóm.


# -----------------------------------------------------------------------------
# 2.11 Apply & Map — Biến Đổi Dữ Liệu
# -----------------------------------------------------------------------------

# --- map() — Áp dụng trên từng phần tử của Series ---

dfmap = pd.DataFrame({
    "Ten":  ["An", "Bình", "Chi", "Duy"],
    "Diem": [8.5, 6.5, 9.0, 5.0]
})
# Dùng dict để map giá trị
rank_dict = {8.5:"Gioi", 6.5:"Kha", 9.0:"Xuat Sac", 5.0:"Trung Binh"}
dfmap["Xep Loai"] = dfmap["Diem"].map(rank_dict)

# Dùng hàm lambda để tính toán
dfmap["Diem/100"] = dfmap["Diem"].map(lambda d : d*10)


# --- apply() — Áp dụng hàm phức tạp hơn ---

dfapl = pd.DataFrame({
    "Ten":   ["An", "Bình", "Chi", "Duy"],
    "Luong": [15,   20,     18,    12],   # triệu
    "Nam":   [3,    5,      4,     2]
})

def xep_cap(luong):
    if luong >=20:
        return "Senior"
    elif luong >= 15:
        return "Mid"
    else:
        return "Junior"
    

dfapl["Cap"] = dfapl["Luong"].apply(xep_cap)

print(dfapl)


# apply trên nhiều cột (axis=1: đọc từng hàng)
def luong_thuc_nhan(hang):
    if hang["Nam"] >= 5:
        bonus = hang["Luong"] * 0.15   # bonus 15%
    else:
        bonus = hang["Luong"] * 0.05   # bonus 5%
    return hang["Luong"] + bonus

dfapl["Luong_thuc_nhan"] = dfapl.apply(luong_thuc_nhan, axis = 1)
print(dfapl)

# -----------------------------------------------------------------------------
# 2.12 Merge & Join — Ghép Bảng
# -----------------------------------------------------------------------------

# Giống JOIN trong SQL — ghép 2 bảng dữ liệu lại với nhau.


don_hang = pd.DataFrame({
    "MaDH":     [1,      2,      3,      4],
    "MaKH":     ["KH01", "KH02", "KH01", "KH03"],
    "SanPham":  ["Áo",   "Quần", "Giày", "Mũ"],
    "GiaTri":   [200000, 350000, 500000, 120000]
})

khach_hang = pd.DataFrame({
    "MaKH":    ["KH01", "KH02", "KH03", "KH04"],
    "TenKH":   ["An",   "Bình", "Chi",  "Duy"],
    "ThanhPho":["HCM",  "HN",   "DN",   "HCM"]
})

# how = outer : giữ tất cả hai bảng
result = pd.merge(don_hang, khach_hang,on ="MaKH", how = "outer"  )
print(result)

# inner join: chỉ giữ hàng KHỚP ở CẢ 2 bảng (mặc định)
result_inner = pd.merge(don_hang, khach_hang, on = "MaKH", how = "inner")
print(result_inner)

# left join : nếu ko ghép được x thì giữ bảng trái
result_left = pd.merge(don_hang, khach_hang, on = "MaKH", how ="left")
print(result_left)

# right join, nếu ko ghép được x thì giữ bảng phải

result_right = pd.merge(don_hang, khach_hang, on = "MaKH", how = "right")
print(result_right)

# concat() : ghép theo chiều dọc - chỉ nối thêm hàng
thang1 = pd.DataFrame({"SP": ["A","B"], "Doanh": [100, 200]})
thang2 = pd.DataFrame({"SP": ["A","C"], "Doanh": [150, 180]})
both1and2 = pd.concat([thang1, thang2], ignore_index = True)
print(both1and2)

# -----------------------------------------------------------------------------
# 2.13 Xử Lý Thời Gian (DateTime)
# -----------------------------------------------------------------------------

dfdaytime = pd.DataFrame({
    "NgayBan": ["2024-01-15", "2024-02-20", "2024-03-05"],
    "Doanh":   [500000,       750000,        300000]
})

# Chuyển string thành datetime
dfdaytime["NgayBan"] = pd.to_datetime(dfdaytime["NgayBan"])
print(dfdaytime)
print(dfdaytime.dtypes)

# Trích xuất thành phần thời gian
dfdaytime["Nam"] = dfdaytime["NgayBan"].dt.year
dfdaytime["Thang"] = dfdaytime["NgayBan"].dt.month
dfdaytime["Ngay"] = dfdaytime["NgayBan"].dt.day
dfdaytime["Thu"] = dfdaytime["NgayBan"].dt.day_name()

print(dfdaytime)

# Lọc theo khoảng thời gian
q1_2024 = dfdaytime[(dfdaytime["NgayBan"] >= "2024-01-15")&
                    (dfdaytime["NgayBan"] <= "2024-03-25")]
print(q1_2024)

# Groupby theo tháng
theo_thang = dfdaytime.groupby(dfdaytime["NgayBan"].dt.month)["Doanh"].sum()
print(f"Theo thang{theo_thang}")
 
# -----------------------------------------------------------------------------
# 2.14 Các Hàm Tiện Ích Hay Dùng
# -----------------------------------------------------------------------------


df14 = pd.DataFrame({
    "SP":     ["Áo", "Quần", "Áo", "Giày", "Quần", "Áo"],
    "Doanh":  [200, 350, 220, 500, 400, 180],
    "Phong":  ["HCM","HN","HCM","DN","HN","HCM"]
})

# value_counts() → đếm số lần xuất hiện của mỗi giá trị
print(df14["SP"].value_counts())
print(df14["Phong"].value_counts())


# unique() và nunique() → các giá trị duy nhất
print(df14["SP"].unique())
print(df14["Phong"].nunique())

# sort_values() → sắp xếp
df14_sorted = df14.sort_values("Doanh", ascending = False) # Giảm dần
df14_multi = df14.sort_values(["Doanh", "Phong"]) #nếu ghi Phòng trước, Doanh sau thì sẽ xét Phòng 
print(f"DF14 Sorted: {df14_sorted}")               # theo thứ tự bảng chữ cái trước
print(f"DF14 Multi Sorted {df14_multi}")

# duplicated() và drop_duplicates()  -> xử lý trùng lặp
print(df14.duplicated())    # False thì ko trùng, True thì trùng
print(df14.drop_duplicates())  # Xóa hàng trùng

# cut() → chia giá trị liên tục thành nhóm (bins)
diem14 = pd.Series([5, 6.5, 7, 8, 8.5, 9, 4, 7.5])
phan_loai = pd.cut(diem14,
                   bins = [0, 5, 6.5, 8, 10],
                   labels = ["Low", "Average","Good","Excellent"])
print(diem14)
print(phan_loai)

diem_xeploai1 = pd.concat([diem14, phan_loai], axis =1)
print(f"Diem xep loai 1{diem_xeploai1}")

diem_xeploai2 = pd.DataFrame({
    "Diem":diem14,
    "Xep Loai": phan_loai
})

print(f"Diem xep loai 2: {diem_xeploai2}")


df14 = pd.DataFrame({
    "SP":     ["Áo", "Quần", "Áo", "Giày", "Quần", "Áo"],
    "Doanh":  [200, 350, 220, 500, 400, 180],
    "Phong":  ["HCM","HN","HCM","DN","HN","HCM"]
})

pivot_table14 = df14.pivot_table(                    # Giống df14.groupby(["Phong", "SP"])["Doanh"].sum()
                                 values = "Doanh",   # Lấy cột "Doanh" để tính toán
                                 index = "Phong",    # Lấy "Phong" làm hàng
                                 columns = "SP",     # Lấy "SP" làm cột
                                 aggfunc = "sum",    # Cách gộp nếu bị trùng
                                 fill_value = 0)     # Nếu ko có data thì thay = 0

print(pivot_table14)

print(df14.groupby(["Phong", "SP"])["Doanh"].sum())


# =============================================================================
# PHẦN 4: MATPLOTLIB & SEABORN
# =============================================================================

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Matplotlib = nền tảng, kiểm soát toàn bộ
# Seaborn    = xây trên Matplotlib, đẹp hơn, dễ hơn, tích hợp tốt với Pandas


# -----------------------------------------------------------------------------
# 4.2 Matplotlib Cơ Bản
# -----------------------------------------------------------------------------

# --- Cấu trúc một biểu đồ Matplotlib ---
fig,ax= plt.subplots(figsize=(8,5))  # tạo khung và khu vực vẽ

thang_x = [1,2,3,4,5,6]
doanhthu_y = [150,200,180,250,300,280]

ax.plot(thang_x, doanhthu_y,
        color ="red",
        marker = "o",
        mfc="black",
        mec="black",
        ms=7,
        linewidth=2,
        label="Doanh thu")

ax.set_title("Doanh thu 6 tháng đầu năm",  # tạo tên biểu đồ
             fontsize=20,
             fontweight="bold",
             fontname="Arial")

ax.set_xlabel("Tháng",       # tạo tên trục x
              fontsize =15,
              fontweight="bold",
              fontname="Arial")

ax.set_ylabel("Triệu Đồng",  # tạo tên trục y
              fontsize=15,
              fontweight="bold",
              fontname="Arial")

ax.legend()  # thêm chú thích
ax.grid(True,alpha=0.3, linewidth=1)  # tạo ô nền background
ax.set_ylim(140,315)

plt.savefig(
    "linechart[1].png",
    dpi=150,              # độ sắc nét
    bbox_inches="tight"   # loại bỏ khoảng trắng
)
ax.tick_params(axis="both",width=0.7)  # ô kẻ đường
plt.tight_layout()    # sắp xếp lại để ko bị đè lên nhau hoặc cắt mất  
plt.show()



# --- Bar Chart — So Sánh Các Nhóm ---

phong    = ["IT", "Kinh doanh", "HR", "Marketing"]
luong_tb2 = [18.5, 21.0, 13.5, 16.0]   # triệu đồng

# Tạo cột
fig, ax = plt.subplots(figsize=(8,5))
bars = ax.bar(phong,luong_tb2,
              color=["#2196F3", "#FF5722", "#4CAF50", "#FF9800"],
              edgecolor="white",
              width=0.8)

# ax.bar_label() : chữ sẽ hiện trên từng cột

# Thêm chữ cho cột
for bar, val in zip(bars, luong_tb2):
    ax.text(bar.get_x()+bar.get_width()/2,
            bar.get_height() + 0.2,
            f"{val:.1f}",
            ha="center",      # căn giữa theo chiều ngang (horizontal)
            va="bottom",      # đáy chữ nằm đúng tọa độ y (vertical)
            fontname="Arial",
            fontweight="bold")

ax.set_title("Lương trung bình của từng ban",
             fontname="Arial",
             fontsize=20,
             fontweight="bold")

ax.set_ylabel("Lương(Triệu Đồng)",
              fontname="Arial",
              fontsize=12,
              fontweight="bold")

ax.set_ylim(0,25)
ax.legend()
plt.savefig(
    "barchart[1].png",
    dpi=150,
    bbox_inches="tight"
)

plt.tight_layout()

plt.show()


# --- Histogram — Phân Phối Dữ Liệu ---

np.random.seed(42)

scores= np.array((np.clip(np.random.normal(loc=6.8,scale=1.67,size=100))).round(1))


fig, ax = plt.subplots(figsize=(8,5))
ax.hist(
    scores,
    color="yellow",
    edgecolor="black",
    bins=15,
    alpha=0.7
)

ax.set_title(
    "Phân phối điểm của học sinh",
    font="Arial",
    fontweight="bold",
    fontsize=25
)

ax.set_xlabel(
    "Điểm",
    font="Arial",
    fontsize=15,
    fontweight="bold"
)

ax.set_ylabel(
    "Sô học sinh",
    font="Arial",
    fontsize=15,
    fontweight="bold"
)

ax.set_ylim(0,25)
ax.set_xlim(0,10)

ax.axvline(
    scores.mean(),
    color="red",
    linestyle="-",
    linewidth=1,
    label=f"Trung bình :{scores.mean():.2f}"    #thêm đường thẳng
)

ax.axvline(
    np.median(scores),
    color="blue",
    linestyle="--",
    linewidth=1,
    label=f"Trung vị {np.median(scores):.2f}"   # thêm đường thẳng
)

ax.legend()

plt.tight_layout()

plt.savefig(
    "histogram[1].png",
    dpi=150,
    bbox_inches="tight"

)
plt.show()


# --- Scatter Plot — Mối Quan Hệ Giữa 2 Biến ---

n=100
experience = np.random.randint(1,16,n)
luong = experience*2 + np.random.randn(n) +8 
fig, ax = plt.subplots(figsize=(8,5))

ax.scatter(
    experience,
    luong,
    color="red",
    edgecolor="white",
    alpha=0.5,
    s=150,
    label=f"IT"
)

m=57
experience_m = np.random.randint(1,16,m)
luong_m = experience_m *1.5 + np.random.randn(m)+8 

ax.scatter(
    experience_m,
    luong_m,
    color="blue",
    edgecolor="white",
    alpha=0.5,
    s=150,
    label=f"Marketing"
)

z1 = np.polyfit(experience,luong,1)
p1 = np.poly1d(z1)
nn1 = np.linspace(1,16,100)
ax.plot(nn1, p1(nn1), color="#27F573", linewidth=3 ,label=f"Trend line IT")

z2 = np.polyfit(experience_m,luong_m,1)
p2 = np.poly1d(z2)
nn2 = np.linspace(1,16,100)
ax.plot(nn2, p2(nn2), color="#F527CF", linewidth=3, label=f"Trend line MKT" )

ax.set_title(
    "Mối quan hệ giữ Ex và Salary của phòng IT, Marketing",
    fontname="Arial",
    fontsize=18,
    fontweight="bold"
)

ax.set_xlabel(
    "Experiences",
    fontname="Arial",
    fontsize=14
)

ax.set_ylabel(
    "Salary",
    fontname="Arial",
    fontsize=14
)

ax.legend()
plt.tight_layout()

plt.savefig(
    "scatter[1].png",
    dpi=150,
    bbox_inches="tight"
)
plt.show()


# --- Subplots — Nhiều Biểu Đồ Cùng Lúc ---

np.random.seed(42)

thang_x = [1,2,3,4,5,6]
doanhthu_y = [150,200,180,250,300,280]

phong    = ["IT", "Kinh doanh", "HR", "Marketing"]
luong_tb2 = [18.5, 21.0, 13.5, 16.0]   # triệu đồng

scores_hist = np.random.normal(loc=6.8, scale=1.7, size = 100).round(1)

n=100
ex_it = np.random.randint(1,15,n)
sa_it = ex_it*2 + np.random.randn(n) + 8

m=75
ex_m = np.random.randint(1,15,n)
sa_m = ex_m*1.5 + np.random.randn(n) + 7.5

fig, axes = plt.subplots(2,2 , figsize=(12,8))  #Subplots 2x2

#linechart1
axes[0,0].plot(thang_x, doanhthu_y,
               color="red",
               marker="o",
               mfc="black",
               ms=5,
               mec="black",
               linewidth=1.4,
               label="Triệu đồng"
)

axes[0,0].set_title("LineChart 1", fontsize=17, fontname="Arial",fontweight="bold")
axes[0,0].set_xlabel("Tháng", fontsize=15, fontname="Arial")
axes[0,0].set_ylabel("Doanh thu", fontsize=15, fontname="Arial")
axes[0,0].grid(True, alpha=0.7, linewidth=1)

#barchart1
axes[0,1].bar(phong, luong_tb2,
              color=["#2196F3", "#FF5722", "#4CAF50", "#FF9800"],
              width=0.67,
              edgecolor="black",
              label=f"Triệu đồng"
)

axes[0,1].set_title("BarChart 1", fontsize=17, fontname="Arial",fontweight="bold")
axes[0,1].set_xlabel("Phòng", fontsize=15, fontname="Arial")
axes[0,1].set_ylabel("Lương TB", fontsize=15, fontname="Arial")

#histogram1
axes[1,0].hist(
    scores_hist,
    color="yellow",
    edgecolor="black",
    bins=20,
    alpha=0.7
)


axes[1,0].set_title("Phân phối điểm của HS", fontsize=17, fontname="Arial", fontweight ="bold")
axes[1,0].set_xlabel("Điểm", fontsize=15, fontname="Arial")
axes[1,0].set_ylabel("Số học sinh", fontsize=15, fontname="Arial")

axes[1,0].axvline(
    scores_hist.mean(),
    color="red",
    linestyle="-",
    linewidth=0.7,
    label=f"Trung bình: {scores_hist.mean():.2f}"
)

axes[1,0].axvline(
    np.median(scores_hist),
    color="blue",
    linestyle=":",
    linewidth=1.2,
    label=f"Trung vị: {np.median(scores_hist):.2f}"
)

#scatter1
axes[1,1].scatter(ex_it, sa_it,
                  color = "blue",
                  s =60,
                  alpha = 0.8,
                  edgecolor="white",
                  label="IT")

axes[1,1].scatter(ex_m, sa_m,
                  color = "red",
                  s =60,
                  alpha = 0.8,
                  edgecolor="white",
                  label="MKT")

axes[1,1].set_title("MQH giữa Ex và Sa của Phòng IT và MKT",fontsize=17, fontname="Arial", fontweight ="bold")
axes[1,1].set_xlabel("Experiences",fontsize=15, fontname="Arial")
axes[1,1].set_ylabel("Salary(Triệu đồng)",fontsize=15, fontname="Arial")

z1 = np.polyfit(ex_it,sa_it,1)
p1 = np.poly1d(z1)
x_line1 = np.linspace(1,16,100)
axes[1,1].plot(x_line1, p1(x_line1), color = "#F527CF", linewidth = 2, label = "IT Trend line")

z2 = np.polyfit(ex_m, sa_m ,1)
p2 = np.poly1d(z2)
x_line2 = np.linspace(1,16,100)
axes[1,1].plot(x_line2, p2(x_line2), color ="#08D453", linewidth = 2, label = "MKT Trend line")


axes[0,0].legend()
axes[0,1].legend()
axes[1,0].legend()
axes[1,1].legend()

plt.suptitle("Synthesis Dashboard [1]", fontsize=23, fontname = "Arial", fontweight="bold", color = "#2A079C")

plt.tight_layout()

plt.savefig(
    "Dashboard[1].png",
    dpi=150,
    bbox_inches ="tight"
)

plt.show()


# -----------------------------------------------------------------------------
# 4.3 Seaborn — Đẹp Hơn, Dễ Hơn
# -----------------------------------------------------------------------------

import seaborn as sns


dfsea = pd.DataFrame({
    "Phong": np.random.choice(["IT","KD","HR"], 100),
    "Luong": np.random.normal(loc=18,scale=4,size=100),
    "Ex":np.random.randint(1,10,100),
    "Gender": np.random.choice(["Male","Female"],100)
})

# --- 1. Histogram + KDE (phân phối) ---


sns.set_theme(style="whitegrid")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(data=dfsea, x = "Luong", bins = 25, color = "blue", kde = "True", ax=ax)
sns.kdeplot(data=dfsea, x="Luong", bw_adjust=0.5)
ax.set_title("Phân phối lương", fontname="Arial", fontsize=25, fontweight="bold")
ax.set_xlabel("Lương(Triệu Đồng)", fontname="Arial", fontsize=15)
ax.set_ylabel("Số nhân viên", fontname="Arial", fontsize=15)
ax.set_ylim(0,14)

plt.tight_layout()

plt.savefig(
    "HistplotSB[1].png",
    dpi=150,
    bbox_inches ="tight"
)

plt.show()


# --- 2. Boxplot (phân phối theo nhóm) ---

dfsea = pd.DataFrame({
    "Phong": np.random.choice(["IT","KD","HR"], 100),
    "Luong": np.random.normal(loc=18,scale=4,size=100),
    "Ex":np.random.randint(1,10,100),
    "Gender": np.random.choice(["Male","Female"],100)
})

fig, ax = plt.subplots(figsize=(8,5))
                                                     # color trong boxplot chỉ được 1 màu, muốn nhiều màu thì phải xài palette
sns.boxplot(data = dfsea, x = "Phong", y = "Luong", palette=["#ED2909", "#0B97F4", "#17E665"], ax = ax)
                                                     # label thì phải xài hue = x x x
ax.set_title("Phân phối lương theo phòng", fontname="Arial", fontsize = 25,fontweight="bold")
ax.set_xlabel("Phòng", fontname="Arial", fontsize=15)
ax.set_ylabel("Lương(Triệu đồng)", fontname="Arial", fontsize = 15)

plt.tight_layout()

plt.savefig(
    "BoxplotSB[1].png",
    dpi=150,
    bbox_inches ="tight"
)

plt.show()


# --- 3. Barplot (trung bình theo nhóm) ---

dfsea = pd.DataFrame({
    "Phong": np.random.choice(["IT","KD","HR"], 100),
    "Luong": np.random.normal(loc=18,scale=4,size=100),
    "Ex":np.random.randint(1,10,100),
    "Gender": np.random.choice(["Male","Female"],100)
})

fig, ax  = plt.subplots(figsize=(8,5))
sns.barplot(data =dfsea, x="Phong", y="Luong", palette="coolwarm",hue="Gender",errorbar = "sd",ax=ax)   # x="Phong" : chia theo phòng ban, hue = "Gender" : tách thêm theo giới tính
ax.set_title("Trung bình lương theo nhóm(Gender)", fontname="Arial", fontsize = 20, fontweight="bold")
ax.set_xlabel("Phòng", fontname="Arial", fontsize=15)
ax.set_ylabel("Lương(Triệu đồng)", fontname="Arial", fontsize=15)
                                                  # barplot tự động tính trung bình
                                                  # đường màu đen là std, càng dài càng chênh lệch nhiều, ngắn thì ko chênh lệch đáng kể
plt.tight_layout()

plt.savefig(
    "BarplotSB[1].png",
    dpi=150,
    bbox_inches ="tight"
)

plt.show()

# --- 4. Scatterplot ---
fig, ax = plt.subplots(figsize=(10,7))

sns.scatterplot(data = dfsea, x="Ex", y="Luong", hue="Phong",palette=["red","skyblue","yellow"],edgecolor="black",s=55, ax=ax)
ax.set_title("Mối quan hệ giữa kinh nghiệm và lương của từng phòng", fontname="Arial",fontsize=20, fontweight="bold")
ax.set_xlabel("Experiences(Years)", fontname="Arial", fontsize=15)
ax.set_ylabel("Salary(Triệu đồng)", fontname="Arial", fontsize=15)
ax.set_ylim(5,31)

plt.tight_layout()

plt.savefig(
    "ScatterplotSB[1].png",
    dpi=150,
    bbox_inches ="tight"
)

plt.show()

# --- 5. Heatmap — Tương Quan Giữa Các Biến ---
corr_matrix = dfsea[["Luong","Ex"]].corr()  # tạo corr matrix

fig, ax = plt.subplots(figsize=(6,5))
#annot = True : hiện số, cmap = colormap, vmin vmax ste limit, fmt = format của số 
sns.heatmap(corr_matrix, annot = True, cmap="coolwarm", vmin=-1, vmax=1,fmt=".2f", ax=ax)
ax.set_title("Tương quan giữa Ex và Salary", fontname="Arial", fontsize=22, fontweight="bold")
plt.tight_layout()

plt.savefig(
    "HeatmapSB[1].png",
    dpi=150,
    bbox_inches ="tight"
)

plt.show()

# --- 6. Pairplot — Tương Quan Tất Cả Các Biến ---
# Dùng khi muốn cái nhìn tổng quan về dataset

sns.pairplot(dfsea[["Luong","Ex"]], diag_kind="kde", diag_kws={"bw_adjust":0.5, "linewidth":1})
plt.suptitle("Pairplot", fontname ="Arial", fontsize = 20, fontweight= "bold")
plt.tight_layout()

plt.savefig(
    "PairplotSB[1].png",
    dpi=150,
    bbox_inches ="tight"
)

plt.show()

#                          --------------------DASHBOARD SEABORN--------------------

import seaborn as sns
import matplotlib.patheffects as pe

np.random.seed(42)
dfsea = pd.DataFrame({
    "Phong": np.random.choice(["IT","KD","HR"], 100),
    "Luong": np.random.normal(loc=18,scale=4,size=100),
    "Ex":np.random.randint(1,10,100),
    "Gender": np.random.choice(["Male","Female"],100)
})

sns.set_theme(style="white")
fig, axes = plt.subplots(2,3,figsize=(20,12), constrained_layout=True)

sns.histplot( data = dfsea, x = "Luong", bins = 25, kde = True, color = "#F52E07", ax = axes[0,0])
sns.kdeplot( data = dfsea, x = "Luong", bw_adjust=0.5, ax = axes[0,0])
axes[0,0].set_title("SeabornHist(Phân phối)", fontsize=18, fontname="Arial", fontweight="bold")
axes[0,0].set_xlabel("Salary(Triệu đồng)", fontsize = 13, fontname="Arial")
axes[0,0].set_ylabel("Số nhân viên", fontsize = 13, fontname="Arial")

sns.boxplot(data=dfsea, x = "Phong", y="Luong", palette=["#FF3300", "#00FFFF","#00FF0D"], ax = axes[0,1])
axes[0,1].set_title("Phân phối lương theo phòng(SB)", fontname="Arial", fontsize=18, fontweight="bold")
axes[0,1].set_xlabel("Phòng", fontname="Arial", fontsize=13)
axes[0,1].set_ylabel("Lương(Triệu đồng)", fontname="Arial", fontsize=13)

sns.barplot(data =dfsea, x = "Phong", y="Luong",hue="Gender", palette="coolwarm",errorbar="sd",ax=axes[0,2])
axes[0,2].set_title("Trung bình lương theo nhóm(Gender)", fontname="Arial", fontsize=15, fontweight="bold")
axes[0,2].set_xlabel("Phòng", fontname="Arial", fontsize=13)
axes[0,2].set_ylabel("Lương(Triệu đồng)", fontname="Arial", fontsize=13)

sns.scatterplot(data=dfsea, x = "Ex", y= "Luong",hue="Phong", palette=["#FF002F","#2EC4FF","#00FF44"], s =57,edgecolor="black",ax=axes[1,0])
axes[1,0].set_title("MQH giữa Salary và Ex(Theo Phòng)", fontname="Arial", fontsize=15, fontweight="bold")
axes[1,0].set_xlabel("Experiences", fontname="Arial", fontsize=13)
axes[1,0].set_ylabel("Lương(Triệu đồng)", fontname="Arial", fontsize=13)

corr_matrix = dfsea[["Luong","Ex"]].corr()
sns.heatmap(corr_matrix, annot=True, vmin=-1, vmax=1, cmap="coolwarm",ax=axes[1,1])
axes[1,1].set_title("Tương quan giữa Ex và Salary(Heatmap)", fontname="Arial", fontsize=15, fontweight="bold", y=1.007)

fig.delaxes(axes[1,2])
plt.suptitle("Synthesis Dashboard [2]", fontname="Arial", fontsize=30, fontweight="bold", color="#FFEA2E", path_effects=[pe.withStroke(linewidth=2.2, foreground="black")])

plt.savefig(
    "DashboardSB[2].png",
    dpi=150,
    bbox_inches ="tight"
)

plt.show()



























































































































































































print("It's not hard, it's just new.")