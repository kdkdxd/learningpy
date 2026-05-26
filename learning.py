
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













































































































































































