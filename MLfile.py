# =============================================================================
# 🤖 MACHINE LEARNING VỚI PYTHON - INTELLIPAAT EDITION
# Tài liệu học hoàn chỉnh từ nền tảng đến thực chiến
# =============================================================================
#
# 📚 Nguồn tham khảo chính:
#   - Intellipaat Data Science Course 2026
#   - Stanford CS229 — Machine Learning (Andrew Ng)
#   - Harvard CS109 — Introduction to Data Science
#   - Hands-On ML — Aurélien Géron, 3rd Ed.
#
# 📚 10 KHÓA HỌC THEO LỘ TRÌNH INTELLIPAAT:
#   ✅ 1. Linux and Python Fundamentals  ← MỚI
#   ✅ 2. Data Wrangling with SQL        ← MỚI
#   ✅ 3. Python with Data Science (NumPy, Pandas, Matplotlib)
#   ✅ 4. Linear Algebra & Advanced Statistics
#   ✅ 5. Machine Learning & Prediction Algorithms
#   ✅ 6. Supervised & Unsupervised Learning
#   ✅ 7. Deep Learning with TensorFlow
#   ✅ 8. Generative AI & Prompt Engineering
#   ✅ 9. Deploying ML Models on Cloud (MLOps)
#   ✅ 10. Data Visualization with Power BI
# =============================================================================

# %% [markdown]
# # 🐧 KHÓA HỌC 1: LINUX AND PYTHON FUNDAMENTALS
# =============================================================================
# ## 1.1 Linux Basics cho Data Scientist

# %%
print("="*70)
print("🐧 LINUX FUNDAMENTALS FOR DATA SCIENCE")
print("="*70)

print("""
📌 TẠI SAO DATA SCIENTIST CẦN BIẾT LINUX?
  • 90% servers chạy Linux (AWS, GCP, Azure)
  • Xử lý file lớn, automation, cron jobs
  • Cài đặt packages, quản lý environment
  • Làm việc với remote servers (SSH)

📁 CÁC LỆNH LINUX CƠ BẢN:

1️⃣ NAVIGATION (Di chuyển)
   pwd                     # Xem thư mục hiện tại
   ls -la                  # Liệt kê file (chi tiết)
   cd /path/to/dir         # Chuyển thư mục
   cd ~                    # Về home directory
   cd ..                   # Lên 1 cấp

2️⃣ FILE OPERATIONS (Thao tác file)
   touch file.txt          # Tạo file rỗng
   cp source dest          # Copy file
   mv old new              # Di chuyển / đổi tên
   rm file.txt             # Xóa file
   rm -rf folder/          # Xóa thư mục (cẩn thận!)
   mkdir new_folder        # Tạo thư mục
   cat file.txt            # Xem nội dung file

3️⃣ PERMISSIONS (Phân quyền)
   chmod 755 script.sh     # Cho phép chạy
   chown user:group file   # Đổi chủ sở hữu

4️⃣ PROCESS MANAGEMENT (Quản lý tiến trình)
   ps aux                  # Xem tiến trình đang chạy
   top                     # Monitor real-time
   kill -9 PID             # Dừng tiến trình
   nohup python train.py & # Chạy background

5️⃣ PACKAGE MANAGEMENT (Cài đặt)
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3-pip

   # CentOS/RHEL
   sudo yum install python3-pip

   # Python packages
   pip install numpy pandas scikit-learn

6️⃣ ENVIRONMENT VARIABLES
   echo $PATH              # Xem PATH
   export PYTHONPATH=/my/path  # Set biến
   source ~/.bashrc        # Reload config

7️⃣ SSH (Remote Access)
   ssh user@server.com     # Kết nối server
   scp file user@server:/path  # Copy file
""")

# %% [markdown]
# ## 1.2 Python Fundamentals cho Data Science

# %%
print("\n" + "="*70)
print("🐍 PYTHON FUNDAMENTALS FOR DATA SCIENCE")
print("="*70)

# --- 1.2.1 Python Basics ---
print("\n[1.2.1 PYTHON BASICS]")

# Variables & Data Types
print("\n📌 VARIABLES & DATA TYPES")
name = "Alice"          # String
age = 25                # Integer
height = 1.75           # Float
is_student = True       # Boolean
scores = [85, 92, 78]   # List
coordinates = (10, 20)  # Tuple (immutable)
person = {"name": "Bob", "age": 30}  # Dictionary

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Is student: {is_student}, Type: {type(is_student)}")
print(f"Scores: {scores}, Type: {type(scores)}")
print(f"Person: {person}, Type: {type(person)}")

# --- 1.2.2 Control Flow ---
print("\n📌 CONTROL FLOW")

# If-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score: {score} → Grade: {grade}")

# Loops
print("\nFor loop:")
for i in range(5):
    print(f"  i = {i}")

print("\nWhile loop:")
count = 0
while count < 3:
    print(f"  count = {count}")
    count += 1

# List comprehension (quan trọng trong DS)
print("\nList comprehension:")
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# --- 1.2.3 Functions ---
print("\n📌 FUNCTIONS")

def calculate_stats(data):
    """Tính mean, median, std của list"""
    if not data:
        return None, None, None
    mean = sum(data) / len(data)
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    variance = sum((x - mean)**2 for x in data) / n
    std = variance ** 0.5
    return mean, median, std

# Lambda functions (hay dùng với Pandas)
square = lambda x: x**2
print(f"Square of 5: {square(5)}")

# --- 1.2.4 Classes & OOP ---
print("\n📌 CLASSES & OOP")

class DataProcessor:
    """Class xử lý dữ liệu cơ bản"""
    def __init__(self, data):
        self.data = data
        self.processed = False
    
    def clean(self):
        """Xóa NaN, outliers"""
        self.data = [x for x in self.data if x is not None and x >= 0]
        self.processed = True
        return self
    
    def normalize(self):
        """Chuẩn hóa về [0,1]"""
        if not self.processed:
            self.clean()
        min_val = min(self.data)
        max_val = max(self.data)
        if max_val - min_val > 0:
            self.data = [(x - min_val) / (max_val - min_val) for x in self.data]
        return self
    
    def stats(self):
        """Trả về thống kê"""
        if not self.data:
            return "No data"
        mean, median, std = calculate_stats(self.data)
        return {
            'mean': mean,
            'median': median,
            'std': std,
            'min': min(self.data),
            'max': max(self.data),
            'n': len(self.data)
        }

# Ví dụ sử dụng
raw_data = [1, 2, None, 3, 4, 5, 100, 6, 7, 8]
processor = DataProcessor(raw_data)
stats = processor.normalize().stats()
print(f"Processed stats: {stats}")

# --- 1.2.5 File I/O ---
print("\n📌 FILE I/O")

# Đọc file
try:
    with open('data.txt', 'r') as f:
        content = f.read()
    print("File read successfully")
except FileNotFoundError:
    print("File not found, creating sample...")
    # Tạo file mẫu
    with open('data.txt', 'w') as f:
        f.write("Hello, Data Science!\n")
        f.write("This is a sample file.\n")
        f.write("Line 3: Python is great!\n")
    print("Sample file created.")

# Đọc CSV-like file
try:
    with open('sample.csv', 'r') as f:
        lines = f.readlines()
        headers = lines[0].strip().split(',')
        data = [line.strip().split(',') for line in lines[1:]]
    print(f"Headers: {headers}")
    print(f"First row: {data[0] if data else 'No data'}")
except FileNotFoundError:
    print("Sample CSV not found, skipping...")

# --- 1.2.6 Error Handling ---
print("\n📌 ERROR HANDLING")

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
        return None
    except TypeError:
        print("❌ Invalid types for division!")
        return None
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / '2' = {safe_divide(10, '2')}")

# --- 1.2.7 Modules & Packages ---
print("\n📌 MODULES & PACKAGES")

# Tạo module đơn giản
# Trong thực tế, lưu vào file math_utils.py
# from math_utils import factorial, gcd

def factorial(n):
    """Tính giai thừa"""
    if n == 0:
        return 1
    return n * factorial(n-1)

def gcd(a, b):
    """Ước chung lớn nhất"""
    while b:
        a, b = b, a % b
    return a

print(f"Factorial of 5: {factorial(5)}")
print(f"GCD of 48 and 18: {gcd(48, 18)}")

# %% [markdown]
# ### 📝 Bài tập nhỏ 1.2
# 1. Viết hàm tính Fibonacci với n bất kỳ
# 2. Tạo class Student với thuộc tính name, scores và phương thức average()
# 3. Đọc file CSV và tính thống kê cơ bản


# =============================================================================
# 🗄️ KHÓA HỌC 2: DATA WRANGLING WITH SQL
# =============================================================================

# %% [markdown]
# ## 2.1 SQL Basics cho Data Science

# %%
print("\n" + "="*70)
print("🗄️ DATA WRANGLING WITH SQL")
print("="*70)

print("""
📌 TẠI SAO DATA SCIENTIST CẦN BIẾT SQL?
  • 80% data nằm trong databases (relational)
  • Lấy dữ liệu trực tiếp từ production DB
  • Join nhiều tables, aggregate data
  • Data cleaning trước khi đưa vào Python

📊 SQL COMMANDS CATEGORIES:

1️⃣ DDL (Data Definition Language)
   CREATE, ALTER, DROP, TRUNCATE
   → Định nghĩa cấu trúc database

2️⃣ DML (Data Manipulation Language)
   SELECT, INSERT, UPDATE, DELETE
   → Thao tác với dữ liệu

3️⃣ DCL (Data Control Language)
   GRANT, REVOKE
   → Phân quyền

4️⃣ TCL (Transaction Control Language)
   COMMIT, ROLLBACK, SAVEPOINT
   → Quản lý transaction
""")

# %% [markdown]
# ## 2.2 SQL Queries cơ bản

# %%
# Tạo database mẫu với SQLite (không cần server)
import sqlite3
import pandas as pd

# --- Tạo database và table mẫu ---
conn = sqlite3.connect(':memory:')  # Lưu trong RAM (cho demo)
cursor = conn.cursor()

# Tạo bảng employees
cursor.execute('''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    salary REAL,
    hire_date TEXT,
    age INTEGER,
    city TEXT
)
''')

# Tạo bảng sales
cursor.execute('''
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    amount REAL,
    sale_date TEXT,
    product TEXT,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
)
''')

# --- Insert dữ liệu mẫu ---
employees_data = [
    (1, 'Alice', 'IT', 75000, '2020-01-15', 28, 'New York'),
    (2, 'Bob', 'Sales', 65000, '2019-06-20', 32, 'Chicago'),
    (3, 'Charlie', 'IT', 80000, '2018-11-01', 35, 'San Francisco'),
    (4, 'Diana', 'HR', 55000, '2021-03-10', 26, 'New York'),
    (5, 'Eve', 'Sales', 70000, '2020-08-15', 30, 'Chicago'),
    (6, 'Frank', 'IT', 90000, '2017-05-01', 40, 'San Francisco'),
    (7, 'Grace', 'HR', 60000, '2022-01-20', 24, 'Boston'),
]

sales_data = [
    (1, 1, 1500, '2023-01-10', 'Laptop'),
    (2, 1, 2200, '2023-01-15', 'Monitor'),
    (3, 2, 3500, '2023-01-12', 'Software'),
    (4, 2, 1800, '2023-02-05', 'Laptop'),
    (5, 3, 5000, '2023-01-20', 'Server'),
    (6, 3, 1200, '2023-02-10', 'Network'),
    (7, 5, 2800, '2023-01-25', 'Software'),
    (8, 5, 3200, '2023-02-15', 'Laptop'),
]

cursor.executemany('INSERT INTO employees VALUES (?,?,?,?,?,?,?)', employees_data)
cursor.executemany('INSERT INTO sales VALUES (?,?,?,?,?)', sales_data)
conn.commit()

print("✅ Database created with sample data!")

# --- 2.2.1 SELECT cơ bản ---
print("\n[2.2.1 SELECT STATEMENTS]")

query1 = """
SELECT name, department, salary
FROM employees
WHERE salary > 65000
ORDER BY salary DESC
"""
df1 = pd.read_sql_query(query1, conn)
print("Employees with salary > 65000:")
print(df1)

# --- 2.2.2 Aggregation ---
print("\n[2.2.2 AGGREGATION]")

query2 = """
SELECT department,
       COUNT(*) as count,
       AVG(salary) as avg_salary,
       MIN(salary) as min_salary,
       MAX(salary) as max_salary,
       SUM(salary) as total_salary
FROM employees
GROUP BY department
"""
df2 = pd.read_sql_query(query2, conn)
print("Department stats:")
print(df2)

# --- 2.2.3 JOIN ---
print("\n[2.2.3 JOINS]")

query3 = """
SELECT e.name,
       e.department,
       COUNT(s.id) as sale_count,
       SUM(s.amount) as total_sales,
       AVG(s.amount) as avg_sale
FROM employees e
LEFT JOIN sales s ON e.id = s.employee_id
GROUP BY e.id
ORDER BY total_sales DESC NULLS LAST
"""
df3 = pd.read_sql_query(query3, conn)
print("Employee sales summary:")
print(df3)

# --- 2.2.4 Subqueries ---
print("\n[2.2.4 SUBQUERIES]")

query4 = """
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
"""
df4 = pd.read_sql_query(query4, conn)
print("Employees above average salary:")
print(df4)

# --- 2.2.5 Window Functions ---
print("\n[2.2.5 WINDOW FUNCTIONS]")

query5 = """
SELECT name,
       department,
       salary,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) as overall_rank
FROM employees
"""
df5 = pd.read_sql_query(query5, conn)
print("Rankings:")
print(df5)

# --- 2.2.6 Date Functions ---
print("\n[2.2.6 DATE FUNCTIONS]")

query6 = """
SELECT name,
       hire_date,
       DATE('now') as today,
       ROUND((JULIANDAY('now') - JULIANDAY(hire_date)) / 365, 1) as years_employed,
       CASE
           WHEN ROUND((JULIANDAY('now') - JULIANDAY(hire_date)) / 365, 1) > 5
           THEN 'Senior'
           WHEN ROUND((JULIANDAY('now') - JULIANDAY(hire_date)) / 365, 1) > 2
           THEN 'Mid'
           ELSE 'Junior'
       END as level
FROM employees
"""
df6 = pd.read_sql_query(query6, conn)
print("Employee tenure:")
print(df6)

# --- 2.2.7 Case Statements ---
print("\n[2.2.7 CASE STATEMENTS]")

query7 = """
SELECT name,
       salary,
       CASE
           WHEN salary >= 80000 THEN 'High'
           WHEN salary >= 60000 THEN 'Medium'
           ELSE 'Low'
       END as salary_level,
       CASE
           WHEN age < 25 THEN 'Gen Z'
           WHEN age < 35 THEN 'Millennial'
           WHEN age < 45 THEN 'Gen X'
           ELSE 'Boomer'
       END as generation
FROM employees
"""
df7 = pd.read_sql_query(query7, conn)
print("Salary levels and generations:")
print(df7)

# %% [markdown]
# ## 2.3 Advanced SQL cho Data Science

# %%
print("\n[2.3 ADVANCED SQL]")

# --- 2.3.1 CTE (Common Table Expressions) ---
print("\n📌 CTE (Common Table Expressions)")

query8 = """
WITH dept_stats AS (
    SELECT department,
           AVG(salary) as dept_avg,
           COUNT(*) as dept_count
    FROM employees
    GROUP BY department
),
high_earners AS (
    SELECT e.name, e.salary, e.department
    FROM employees e
    JOIN dept_stats d ON e.department = d.department
    WHERE e.salary > d.dept_avg
)
SELECT *
FROM high_earners
"""
df8 = pd.read_sql_query(query8, conn)
print("Employees earning above department average:")
print(df8)

# --- 2.3.2 Pivot Table (cross tabulation) ---
print("\n📌 PIVOT TABLE")

query9 = """
SELECT department,
       COUNT(CASE WHEN age < 30 THEN 1 END) as under_30,
       COUNT(CASE WHEN age BETWEEN 30 AND 39 THEN 1 END) as age_30_39,
       COUNT(CASE WHEN age >= 40 THEN 1 END) as over_40
FROM employees
GROUP BY department
"""
df9 = pd.read_sql_query(query9, conn)
print("Age distribution by department:")
print(df9)

# --- 2.3.3 Recursive CTE ---
print("\n📌 RECURSIVE CTE")

# Tạo bảng employee hierarchy
cursor.execute('''
CREATE TABLE emp_hierarchy (
    id INTEGER PRIMARY KEY,
    name TEXT,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES emp_hierarchy(id)
)
''')

hierarchy_data = [
    (1, 'CEO', None),
    (2, 'VP_IT', 1),
    (3, 'VP_Sales', 1),
    (4, 'Manager_IT', 2),
    (5, 'Manager_Sales', 3),
    (6, 'Developer_1', 4),
    (7, 'Developer_2', 4),
    (8, 'Sales_Rep_1', 5),
    (9, 'Sales_Rep_2', 5),
]
cursor.executemany('INSERT INTO emp_hierarchy VALUES (?,?,?)', hierarchy_data)
conn.commit()

query10 = """
WITH RECURSIVE emp_tree AS (
    -- Base case
    SELECT id, name, manager_id, 0 as level,
           CAST(name AS TEXT) as path
    FROM emp_hierarchy
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive case
    SELECT e.id, e.name, e.manager_id, t.level + 1,
           t.path || ' > ' || e.name as path
    FROM emp_hierarchy e
    JOIN emp_tree t ON e.manager_id = t.id
)
SELECT name, level, path
FROM emp_tree
ORDER BY path
"""
df10 = pd.read_sql_query(query10, conn)
print("Organization hierarchy:")
print(df10)

# --- 2.3.4 Stored Procedures (simulated with Python) ---
print("\n📌 STORED PROCEDURES")

def get_sales_summary(conn, min_amount=1000):
    """Hàm Python mô phỏng stored procedure"""
    query = """
    SELECT e.department,
           COUNT(s.id) as sales_count,
           SUM(s.amount) as total_sales,
           AVG(s.amount) as avg_sales
    FROM employees e
    JOIN sales s ON e.id = s.employee_id
    WHERE s.amount > ?
    GROUP BY e.department
    ORDER BY total_sales DESC
    """
    return pd.read_sql_query(query, conn, params=(min_amount,))

print("Sales summary (min > 1000):")
print(get_sales_summary(conn, 1000))

print("\nSales summary (min > 2000):")
print(get_sales_summary(conn, 2000))

# --- 2.3.5 SQL trong Data Science Pipeline ---
print("\n📌 SQL IN DS PIPELINE")

# Ví dụ: Lấy dữ liệu → ETL → Phân tích
def etl_pipeline(conn, target_employee_id):
    """ETL Pipeline mô phỏng"""
    
    # Extract: Lấy dữ liệu
    query_extract = """
    SELECT e.name, e.department, e.salary,
           s.amount, s.sale_date, s.product
    FROM employees e
    JOIN sales s ON e.id = s.employee_id
    WHERE e.id = ?
    """
    df_raw = pd.read_sql_query(query_extract, conn, params=(target_employee_id,))
    
    # Transform: Xử lý dữ liệu
    df_transformed = df_raw.copy()
    df_transformed['sale_date'] = pd.to_datetime(df_transformed['sale_date'])
    df_transformed['year'] = df_transformed['sale_date'].dt.year
    df_transformed['month'] = df_transformed['sale_date'].dt.month
    df_transformed['bonus'] = df_transformed['amount'] * 0.05  # 5% bonus
    
    # Load: Tổng hợp
    summary = {
        'employee': df_transformed['name'].iloc[0],
        'department': df_transformed['department'].iloc[0],
        'salary': df_transformed['salary'].iloc[0],
        'total_sales': df_transformed['amount'].sum(),
        'avg_sale': df_transformed['amount'].mean(),
        'total_bonus': df_transformed['bonus'].sum(),
        'sale_count': len(df_transformed),
        'top_product': df_transformed['product'].mode().iloc[0] if not df_transformed.empty else 'None'
    }
    
    return pd.DataFrame([summary])

# Test ETL
etl_result = etl_pipeline(conn, 1)
print("ETL Pipeline result:")
print(etl_result.T)

# --- 2.3.6 SQL Best Practices ---
print("\n📌 SQL BEST PRACTICES")

print("""
✅ BEST PRACTICES CHO DATA SCIENTIST:

1️⃣ INDEXING
   CREATE INDEX idx_employee_id ON sales(employee_id);
   → Đẩy nhanh query JOIN

2️⃣ AVOID SELECT *
   SELECT specific_columns → Dùng ít memory hơn

3️⃣ USE EXPLAIN ANALYZE
   → Xem execution plan, tối ưu query

4️⃣ LIMIT FOR DEBUG
   SELECT * FROM large_table LIMIT 100
   → Không crash máy khi test

5️⃣ USE TEMPORARY TABLES FOR COMPLEX QUERIES
   CREATE TEMP TABLE temp_stats AS
   SELECT ...

6️⃣ PARAMETERIZED QUERIES
   → Tránh SQL injection, safe hơn

7️⃣ USE CTEs FOR READABILITY
   → Dễ đọc hơn subquery lồng nhau

8️⃣ DATE FUNCTIONS
   → WHERE date_column BETWEEN '2023-01-01' AND '2023-12-31'
""")

# --- 2.3.7 SQL vs Pandas Comparison ---
print("\n📌 SQL VS PANDAS COMPARISON")

print("""
+------------------+----------------------+----------------------+
| Operation        | SQL                  | Pandas               |
+------------------+----------------------+----------------------+
| Select rows      | SELECT * FROM table  | df.head()            |
| Filter           | WHERE condition      | df[df['col'] > x]    |
| Group by         | GROUP BY col         | df.groupby('col')    |
| Aggregate        | AVG(), SUM(), COUNT()| df.groupby().mean()  |
| Join             | JOIN ... ON          | pd.merge()           |
| Sort             | ORDER BY col         | df.sort_values()     |
| Limit            | LIMIT n              | df.head(n)           |
| Distinct         | SELECT DISTINCT      | df['col'].unique()   |
+------------------+----------------------+----------------------+

💡 QUY TẮC CHỌN:
   • SQL: Dữ liệu lớn (>1GB), cần hiệu năng
   • Pandas: Dữ liệu vừa, cần tính toán phức tạp
   • Kết hợp: Lấy data bằng SQL, xử lý bằng Pandas
""")

# Close connection
conn.close()
print("\n✅ SQLite connection closed")

# %% [markdown]
# ### 📝 Bài tập nhỏ 2.3
# 1. Viết query tìm top 3 employees có doanh số cao nhất mỗi department
# 2. Tạo báo cáo doanh số theo tháng với cumulative sum
# 3. Kết hợp SQL + Pandas để tính moving average của sales


# =============================================================================
# 🚀 TIẾP TỤC VỚI CÁC KHÓA HỌC CÒN LẠI...
# =============================================================================

# %% [markdown]
# ## 📚 CÁC KHÓA HỌC TIẾP THEO

# %%
print("""
╔════════════════════════════════════════════════════════════════╗
║            📚 TIẾP TỤC VỚI CÁC KHÓA HỌC CÒN LẠI              ║
╚════════════════════════════════════════════════════════════════╝

✅ Khóa học 3: Python with Data Science
   → NumPy, Pandas, Matplotlib, Seaborn
   → Đã có trong các file riêng: numpy_summary.html, pandas_summary.html, dseekMatplotlibSB.html

✅ Khóa học 4: Linear Algebra & Advanced Statistics
   → Vectors, Matrices, Eigenvalues, Probability Distributions
   → Bayesian Theorem, Hypothesis Testing
   → Đã có trong file này (Phần 2)

✅ Khóa học 5-6: Machine Learning (Supervised + Unsupervised)
   → Regression, Classification, Clustering
   → Đã có trong file này (Phần 3-8)

✅ Khóa học 7: Deep Learning with TensorFlow
   → Neural Networks, CNNs, RNNs, Transfer Learning
   → Đã có trong file này (Phần 10)

✅ Khóa học 8: Generative AI & Prompt Engineering
   → LLMs, OpenAI API, Prompt Techniques
   → Đã có trong file này (Phần 13)

✅ Khóa học 9: Deploying ML Models on Cloud (MLOps)
   → FastAPI, Docker, Cloud Deployment
   → Đã có trong file này (Phần 12)

✅ Khóa học 10: Data Visualization with Power BI
   → (Có thể thêm nếu cần)
""")

print("\n🎉 KHÓA HỌC 1 & 2 ĐÃ ĐƯỢC BỔ SUNG HOÀN CHỈNH!")
print("📊 CHÚC BẠN HỌC TỐT VÀ THÀNH CÔNG!")