#miniprojects

# ============================================================
# MINI PROJECT: Personal Expense Analyzer
# Concepts: list, dict, loop, comprehension, lambda, f-string
# ============================================================

#  INPUT DATA
# Each transaction is a dict, all transactions collected in a list
transactions = [
    {"month": 1, "category": "Food",          "amount": 150000},
    {"month": 1, "category": "Transport",     "amount": 50000},
    {"month": 1, "category": "Food",          "amount": 200000},
    {"month": 2, "category": "Entertainment", "amount": 300000},
    {"month": 2, "category": "Transport",     "amount": 80000},
    {"month": 2, "category": "Food",          "amount": 120000},
    {"month": 3, "category": "Entertainment", "amount": 150000},
    {"month": 3, "category": "Food",          "amount": None},   # missing value
    {"month": 3, "category": "Transport",     "amount": -999},   # error code
]

#DATA CLEANING
cleaned_tran = [t for t in transactions if t["amount"] is not None and t["amount"] != -999 ]
print(f"Total raw transactions     : {len(transactions)}")
print(f"Total Valid transactions   : {len(cleaned_tran)}")
print(f"Removed transactions       : {len(transactions)- len(cleaned_tran)} ")
print()

#DATA ANALISICS
amount = [a["amount"] for a in cleaned_tran]
print(f"Highest: {max(amount)}")
print(f"Lowest: {min(amount)}")
print(f"Total: {sum(amount)}")
print(f"Average: {sum(amount)/len(amount)}")

#DICT GROUPTING
spending = {}
for t in cleaned_tran:
    cat=t["category"]
    amt=t["amount"]
    if cat not in spending:
        spending[cat]=0
        spending[cat]+=amt

spending = {
    "Food"         : 470000,
    "Transport"    : 130000,
    "Entertainment": 450000,
}

total_spend = sum(spending.values())
mean = total_spend/len(spending)

#PERCENTAGE
percentage = {
    cat: round(amt/total_spend*100, 2)
    for cat,amt in spending.items()
}

top_category = max(spending, key=lambda x:spending[x])

#Which month exceeded the monthly avg?
monthly_total = {}
for t in cleaned_tran:
    m = t["month"]
    amt =t["amount"]
    if m not in monthly_total:
        monthly_total[m]=0
        monthly_total[m]+=amt

avg = sum(monthly_total.values())/len(monthly_total)
busy_months = [f"Month:{m}" for m,b in monthly_total.items()
               if b>avg]

sorted_spending = dict(sorted(spending.items(), key=lambda x : x[1]))
top3 = list(sorted_spending.items())[:3]

month_values = list(monthly_total.values())

growth=[]
for i in range(1, len(month_values)):
    g = month_values[i]-month_values[i-1]/month_values[i-1]*100
    growth.append(round(g, 1))
#25%   70%


#=== Monthly Growth (MoM) ===
#Month 1 → Month 2: ▲ 25.0%
#Month 2 → Month 3: ▼ -70.0%

#MoM
for i,g in enumerate(growth):
    arrow ="^"if g>0 else "v"
    print(f"Month:{i+1}->{i+2}={g}")
print()

def spending_label(amount):
    if amount>=200000:
        return "High"
    elif amount>=100000:
        return "Medium"
    else:
        return "Low"

labeled = [
    {**t, "label": spending_label(t["amount"])}
    for t in cleaned_tran
]

         #=== Transaction Labels ===
#Month 1 | Food            |  150,000 | Medium
#Month 1 | Transport       |   50,000 | Low
#Month 1 | Food            |  200,000 | High
#Month 2 | Entertainment   |  300,000 | High
#Month 2 | Transport       |   80,000 | Low
#Month 2 | Food            |  120,000 | Medium
#Month 3 | Entertainment   |  150,000 | Medium


#Count transactions per label:
labeled={}
for l in labeled:
    lbl = l["label"]
    if lbl not in labeled:
        lbl["label"]=0
        lbl["label"]+=1

spending = {
    "Food"         : 470000,
    "Transport"    : 130000,
    "Entertainment": 450000,
}

budget = {
    "Food"         : 400000,
    "Transport"    : 200000,
    "Entertainment": 300000,
}

warning=[]
for cat,limit in budget.items():
    actual = spending.get(cat, 0)
    diff = actual - limit
    if diff > 0:
        status = "OVER BUDGET"
        warning.append(cat)
    else:
        status = "OK"
            

print(f"{cat:<15}: spent {actual:>8,.0f} / budget {limit:>8,.0f}  {status}")
print()
if warning:
    print(f"Categories over budget: {warning}")
else:
    print("All categories within budget!")

# ===============================================================================
# MINI PROJECT: Sports Analytics Lab
# Concepts: Numpy, Broadcasting, std, Correlation, Monte Carlo, Z score, Weighted
# ===============================================================================


import numpy as np


players = ["Ronaldo", "Messi", "Neymar", "Mbappe", "Lamine Yamal", "Haaland"]
stats = np.array([
    [28,  7, 110,  620,  9.8, 33.5],  # Ronaldo
    [18, 19,  72, 1380,  9.2, 30.8],  # Messi
    [16, 14,  81,  890,  9.9, 32.6],  # Neymar
    [34, 11, 138,  740, 10.8, 36.2],  # Mbappe
    [12, 16,  68,  920, 10.1, 35.8],  # Lamine Yamal
    [38,  8, 152,  480, 10.5, 34.9],  # Haaland ← thêm vào
])


# TASK 1 : Statistic
col_mean = np.mean(stats, axis = 0 )
col_std =np.std(stats, axis = 0)

mn_score = np.min(stats[:,0])
mx_score =np.max(stats[:,0])

print(f"Mean:{col_mean}")
print(f"Standard Devitation:{col_std}")
print(f"Lowest Score: {mn_score}")
print(f"Highest Score: {mx_score}")

# TASK 2: Normalize Data
Z_score = (stats - col_mean)/col_std
normalized = (stats - stats.min(axis =0)) / (stats.max(axis =0) - stats.min(axis =0))

print(f"Z score:{Z_score}")
print(f"Normalization{normalized}")

# TASK 3 : Performance Score
weights = np.array([0.35, 0.20, 0.15, 0.10, 0.10, 0.10])
scores = normalized @ weights
print(f"Scores:{scores}")
#so sánh chỉ số về mọi mặt một cách công bằng nhất
#Z score giúp so sánh công bằng về mặt thông kê
#Weighted giúp so sánh công bằng theo mức độ quan trọng

# TASK 4 : Correlation Analysis

goals = stats[:, 0]
shots = stats[:, 2]
corr = np.corrcoef(goals, shots)  #trả lời câu hỏi: goals và shot có tương quan ko
print(f"Correlation between Goals and Shots:{corr}")  

corr_matrix = np.corrcoef(stats)
print(f"Correlation Matrix compares players profiles{np.round(corr_matrix,3)}")
#so sánh các hàng
#câu hỏi: 2 cầu thủ có profile giống nhau không
#output: matrix 6x6 theo cầu thủ

corr_matrix2 = np.corrcoef(stats.T)
print(f"Correclation Matrix compares players abilities: {corr_matrix2}")

# TASK 5 : Monte Carlo Simulation

current_goals = stats[:,0]
mean_goals = np.mean(current_goals)
std_goals = np.std(current_goals)

N_simulations = 10

np.random.seed(42) #np.random.seed()  #Làm cho giữ liệu cố định trong mỗi lần thử
simulation = np.random.normal(
    loc = current_goals,    #trung bình
    scale = std_goals*0.3,  #devitation
    size = (N_simulations, 6)  #10 hàng, 6 cột
)

print(f"Monte Carlo:{simulation}")

winners = np.argmax(simulation, axis = 1)
probs = np.bincount(winners, minlength=6) / N_simulations
#bincount = count how many time winners won

print(f"Winner's indexes:{winners}")

print(probs)
for i, p in enumerate(probs):
    print(f"{players[i]}:{p*100:.1f}% change")


# =============================================================================
#  MINI PROJECT: PHÂN TÍCH DỮ LIỆU NHÂN VIÊN
#  Bao gồm: 2.1 → 2.8 (Series, DataFrame, read_csv, Sampling, loc/iloc,
#           Filtering, Thêm/Sửa/Xóa cột)
# =============================================================================


import numpy as np
import pandas as pd

print ("=== Employee Data Analysis ===")

# =============================================================================
# TẠO DỮ LIỆU GIẢ (thay cho việc đọc file CSV)
# Trong thực tế: pd.read_csv("nhan_vien.csv")
# =============================================================================

np.random.seed(42)
df = pd.DataFrame({
    "Code": ["NV001","NV002","NV003","NV004","NV005",
             "NV006","NV007","NV008","NV009","NV010"],
    "Name": ["An", "Bình", "Chi", "Duy", "Em",
             "Hà", "Khoa", "Linh", "Minh", "Phúc"],
    "Phong": ["IT", "KD", "IT", "HR", "KD",
              "HR", "IT", "KD", "HR", "IT"],
    "Luong":[15, 20, 18, 12, 22,
             14, 19, 13, 21, 17],
    "Experience": [3, 5, 4, 2, 6,
                   3, 5, 2, 7, 4],
    "KPI": [8.5, 9.0, 8.0, 7.5, 9.5,
            7.0, 8.8, 7.2, 9.2, 8.3],
    "Gender": ["M", "M", "F", "M", "F",
               "F", "M", "F", "M", "F"]
})

print(df)

# =============================================================================
# KHÁM PHÁ DỮ LIỆU ĐẦU TIÊN (2.3)
# Luôn làm điều này đầu tiên khi nhận dataset mới!
# =============================================================================
print(f"Shape of Dataset:{df.shape}")
print(f"First 5 rows:\n{df.head(5)}")
print(f"Data Type:{df.dtypes}")
print(f"Data Info:{df.info()}")
print(f"Describe Dataset:{df.describe()}")

# =============================================================================
# LÀM VIỆC VỚI SERIES (2.2)
# Mỗi cột trong DataFrame là 1 Series
# =============================================================================

luong = df["Luong"]
print("Analysics Salary")
print(f"Total Salary:{luong.sum()} trieu vnd")
print(f"Mean Salary:{luong.mean():.1f} trieu vnd")
print(f"Median Salary:{luong.median()} trieu vnd")
print(f"Max Salary:{luong.max()} trieu vnd -> {luong.idxmax()}")
print(f"Min Salary:{luong.min()} trieu vnd -> {luong.idxmin()}")

salary_pct = luong/luong.sum()*100
print("Salary percentage of each person:")
print(f"{salary_pct.round(1)}%")

# =============================================================================
# SAMPLING: LẤY MẪU (2.5)
# =============================================================================
 
ex_random = df.sample(n=5, random_state = 42)
print(f"Ex Random{ex_random[["Name","Phong","Luong"]]}")

ex_stratified = df.groupby("Phong", group_keys =False).sample(
    frac = 0.5,
    random_state = 42
)
print(f"Ex Stratified:{ex_stratified}")

print("50 percent each room:")
print(ex_stratified[["Name", "Phong", "Luong"]])
print("Number of people in Ex Stratified:")
print(ex_stratified["Phong"].value_counts())

# =============================================================================
# TRUY CẬP DỮ LIỆU VỚI LOC & ILOC (2.6)
# =============================================================================

print(f"First Line:{df.loc[0]}")
print(f"First 3 Lines, 2 Columns:{df.loc[0:2, ["Name", "Luong"]]}")
print(f"Row 0-2, Columns 1-3:{df.iloc[0:3, 1:4]}")

df_indexed = df.set_index("Code")
print(f"After indexed:{df_indexed.loc["NV003"]}")

# =============================================================================
# LỌC DỮ LIỆU (2.7)
# =============================================================================

nv_it = df[df["Phong"]=="IT"]
print(nv_it)
print(f"Number of It workers:{len(nv_it)}")
print(nv_it[["Name", "Luong", "Experience"]])


it_senior = df[(df["Phong"]=="IT")&(df["Experience"] >=4)]
print(f"IT workers with 4 years experience:{it_senior}")
print(f"Number of Senior IT workers:{len(it_senior)}")
print(it_senior[["Name","Experience","Luong"]])

kd_it = df[df["Phong"].isin(["KD","IT"])]
print(f"KD and IT workers:{kd_it}")

medium_salary = df[df["Luong"].between(15,20)]
print(f"Number of workers who have medium salary:{len(medium_salary)}")
print(medium_salary[["Name", "Phong", "Luong"]])

not_hr = df[~(df["Phong"]=="HR")]
print(f"Not HR:{not_hr}")

# =============================================================================
# THÊM / SỬA / XÓA CỘT (2.8)
# =============================================================================
 
bonus_pct = np.select(
    condlist =[
        df["Phong"] == "IT",
        df["Phong"] == "KD",
        df["Phong"] == "HR"
    ],
    choicelist = [0.20, 0.25, 0.15],
    default = 0
)

df["Bonus"] = (df["Luong"] * bonus_pct).round(1)
df["Total Salary"] = df["Luong"]+ df["Bonus"]

print(f"Bonus and Total Salary: {df['Bonus']} {df["Total Salary"]} ")
print(df)

df["Rank"] = np.select(
    condlist =[
        df["Luong"] >=20,
        df["Luong"] >=15,
        df["Luong"] <15
    ],
    choicelist = ["High", "Medium", "Low"],
    default = "Unidentified"
)

print(df)

df.loc[df["Name"] == "An", "Luong"] = 17
df.loc[df["Name"] == "Duy", "Luong"] = 23
df.loc[df["Name"] == "An", "Total Salary"] = 17 + df.loc[df["Name"] == "An", "Bonus"]
print(df)

df = df.rename(columns ={"Luong":"Salary"})
df = df.drop(columns = "Gender")

print(df)

print(df.columns.to_list())

































































































































































































































































































































































































































