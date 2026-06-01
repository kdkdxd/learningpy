# =============================================================================
#  PYTHON CHO DATA SCIENCE
#  NumPy · Pandas · Matplotlib · Seaborn · Scipy.Stats
# =============================================================================
#
#  Cách dùng tài liệu này:
#  Mỗi khái niệm theo thứ tự: (1) Vấn đề → (2) Giải pháp → (3) Code có chú thích
#                              → (4) Ví dụ thực tế → (5) Tóm tắt 1 dòng
#  Đừng chỉ đọc — hãy tự gõ lại từng đoạn code vào máy.
#
#  Dựa theo: Harvard CS109 / CS109x — Introduction to Data Science with Python
#  Sách đi kèm: An Introduction to Statistical Learning (statlearning.com)
# =============================================================================

# =============================================================================
# KHUNG TƯ DUY: 5 FACETS CỦA DATA SCIENCE (Harvard CS109)
# =============================================================================
#
#  Harvard không dạy Python như một ngôn ngữ lập trình —
#  họ dạy cách TƯ DUY VỀ DỮ LIỆU. Mọi dự án DS đều đi qua 5 bước:
#
#  ┌──────────────────────────────────────────────────────────────────┐
#  │  1. DATA COLLECTION  │ Thu thập, scraping, sampling dữ liệu     │
#  │  2. DATA MANAGEMENT  │ Làm sạch, xử lý, lưu trữ (Pandas)        │
#  │  3. EDA              │ Khám phá → đặt câu hỏi → tìm pattern     │
#  │  4. PREDICTION       │ Hồi quy, phân loại (sklearn — sau này)   │
#  │  5. COMMUNICATION    │ Visualize + kể câu chuyện từ dữ liệu     │
#  └──────────────────────────────────────────────────────────────────┘
#
#  Tài liệu này bao phủ Bước 1–3 và 5. Bước 4 (ML) là tài liệu tiếp theo.
# =============================================================================


# =============================================================================
# PHẦN 1: NUMPY
# =============================================================================

# -----------------------------------------------------------------------------
# 1.1 Tại sao cần NumPy?
# -----------------------------------------------------------------------------

# VẤN ĐỀ: list Python thông thường không hỗ trợ phép tính vectorized
diem = [6, 7, 8, 5, 9]

# ❌ Cách này sẽ BÁO LỖI:
# diem + 5  → TypeError

# ✅ Phải làm thủ công từng phần tử:
diem_bonus = [d + 5 for d in diem]
print(diem_bonus)  # [11, 12, 13, 10, 14]

# Với 5 phần tử thì ổn. Nhưng trong Data Science bạn làm với
# HÀNG TRIỆU dòng → vòng lặp for sẽ cực kỳ chậm.

# GIẢI PHÁP: NumPy
import numpy as np

diem = np.array([6, 7, 8, 5, 9])
diem_bonus = diem + 5          # ✅ Hoạt động luôn, cực nhanh
print(diem_bonus)              # [11 12 13 10 14]

# Tại sao NumPy nhanh hơn?
# NumPy lưu dữ liệu trong bộ nhớ theo kiểu C (liên tục, cùng kiểu dữ liệu),
# trong khi list Python lưu từng phần tử riêng lẻ.
# NumPy tính toán ở cấp độ C/Fortran, không qua vòng lặp Python.

# ✏️  Tóm tắt 1 dòng: NumPy = mảng số siêu nhanh, thay thế list khi tính toán toán học.


# -----------------------------------------------------------------------------
# 1.2 Tạo Array
# -----------------------------------------------------------------------------

import numpy as np

# --- Mảng 1 chiều (1D) ---
doanh_thu = np.array([120, 250, 310, 180, 400])
#                      T1   T2   T3   T4   T5  (triệu đồng)

print(doanh_thu)        # [120 250 310 180 400]
print(doanh_thu.shape)  # (5,)   → 5 phần tử, 1 chiều
print(doanh_thu.dtype)  # int64  → kiểu số nguyên 64-bit

# --- Mảng 2 chiều (2D) — như bảng Excel ---
# Mỗi hàng = 1 nhân viên, mỗi cột = doanh thu theo quý
doanh_thu_nv = np.array([
    [120, 150, 200, 180],   # nhân viên A
    [200, 220, 190, 210],   # nhân viên B
    [95,  110, 130, 120],   # nhân viên C
])

print(doanh_thu_nv.shape)   # (3, 4) → 3 hàng, 4 cột
print(doanh_thu_nv.ndim)    # 2      → 2 chiều
print(doanh_thu_nv.size)    # 12     → tổng số phần tử

# --- Các cách tạo array nhanh ---

# np.zeros → tạo mảng toàn số 0
# Dùng khi: khởi tạo mảng kết quả trước khi tính
ket_qua = np.zeros(5)
print(ket_qua)    # [0. 0. 0. 0. 0.]

# np.ones → tạo mảng toàn số 1
don_gia = np.ones(4) * 50000  # tất cả giá đều 50,000đ
print(don_gia)    # [50000. 50000. 50000. 50000.]

# np.arange → tạo dãy số (giống range() nhưng ra array)
# Cú pháp: np.arange(start, stop, step)
ngay = np.arange(1, 8)           # ngày 1 đến 7
print(ngay)       # [1 2 3 4 5 6 7]

chia_nho = np.arange(0, 1, 0.1)  # từ 0 đến 1, bước 0.1
print(chia_nho)   # [0.  0.1 0.2 ... 0.9]

# np.linspace → chia đều n điểm trong khoảng [a, b]
# Dùng khi: vẽ đồ thị, chia khoảng đều nhau
x = np.linspace(0, 100, 5)       # 5 điểm từ 0 đến 100
print(x)          # [  0.  25.  50.  75. 100.]

# np.random.rand → số ngẫu nhiên từ 0 đến 1
# Dùng khi: tạo dữ liệu giả để test
mau_test = np.random.rand(3, 3)  # ma trận 3x3 ngẫu nhiên

# ✏️  Tóm tắt 1 dòng: array() tạo từ dữ liệu có sẵn;
#     zeros/ones/arange/linspace tạo dữ liệu mẫu.


# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
# 1.4 Operations — Tính toán trên Array
# -----------------------------------------------------------------------------

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
#  [3 6]]l


# =============================================================================
# PHẦN 2: PANDAS
# =============================================================================

# Pandas giải quyết giới hạn của NumPy:
# - NumPy chỉ chứa một kiểu dữ liệu (toàn số hoặc toàn string)
# - NumPy không có tên cột/hàng → khó đọc
# - NumPy không xử lý được dữ liệu thiếu (NaN)
# - NumPy không đọc được file CSV, Excel
# Pandas là thư viện số 1 của Data Science — bạn sẽ dùng nó HÀNG NGÀY.

import pandas as pd

# -----------------------------------------------------------------------------
# 2.2 Series — Mảng 1 chiều có nhãn
# -----------------------------------------------------------------------------

# Tạo Series từ list — tự động đánh index 0, 1, 2...
diem_toan = pd.Series([8.0, 7.5, 9.0, 6.5, 8.5])
print(diem_toan)
# 0    8.0
# 1    7.5
# 2    9.0
# 3    6.5
# 4    8.5
# dtype: float64

# Tạo Series với INDEX tự đặt (quan trọng!)
# Dùng khi: tên học sinh, mã sản phẩm, ngày tháng...
diem_toan = pd.Series(
    [8.0, 7.5, 9.0, 6.5, 8.5],
    index=["An", "Bình", "Chi", "Duy", "Em"]
)
print(diem_toan)
# An      8.0
# Bình    7.5
# Chi     9.0
# Duy     6.5
# Em      8.5

# Tạo từ dictionary — key tự động thành index
chi_tieu = pd.Series({
    "Ăn uống":   2500000,
    "Thuê nhà":  3000000,
    "Di chuyển": 500000,
    "Giải trí":  800000
})
print(chi_tieu)

# --- Truy cập dữ liệu trong Series ---

# Truy cập bằng nhãn (label)
print(chi_tieu["Ăn uống"])    # 2500000
print(chi_tieu["Thuê nhà"])   # 3000000

# Truy cập bằng vị trí số
print(chi_tieu.iloc[0])       # 2500000  (phần tử đầu tiên)
print(chi_tieu.iloc[-1])      # 800000   (phần tử cuối)

# Slicing
print(chi_tieu["Ăn uống":"Di chuyển"])  # 3 mục đầu (KÈM điểm dừng!)
print(chi_tieu.iloc[0:2])               # 2 mục đầu (KHÔNG kèm điểm dừng)

# Boolean indexing
tieu_lon = chi_tieu[chi_tieu > 1000000]
print(tieu_lon)
# Ăn uống    2500000
# Thuê nhà   3000000

# --- Tính toán trên Series ---

print(chi_tieu.sum())    # 6800000 → tổng chi tiêu
print(chi_tieu.mean())   # 1700000 → trung bình
print(chi_tieu.max())    # 3000000 → lớn nhất
print(chi_tieu.min())    # 500000  → nhỏ nhất

# idxmax / idxmin → trả về TÊN (index), không phải giá trị
print(chi_tieu.idxmax()) # "Thuê nhà"
print(chi_tieu.idxmin()) # "Di chuyển"

# Tính % mỗi khoản trên tổng chi tiêu
phan_tram = chi_tieu / chi_tieu.sum() * 100
print(phan_tram.round(1))
# Ăn uống      36.8
# Thuê nhà     44.1
# Di chuyển     7.4
# Giải trí     11.8

# ✏️  Tóm tắt 1 dòng: Series = cột dữ liệu có tên hàng (index),
#     có thể tính toán, lọc như NumPy.


# -----------------------------------------------------------------------------
# 2.3 DataFrame — Trái tim của Pandas
# -----------------------------------------------------------------------------

# DataFrame = bảng dữ liệu 2 chiều, giống Excel.
# Mỗi cột là một Series, tất cả dùng chung index (tên hàng).

import pandas as pd

# Tạo DataFrame từ dictionary
# Key = tên cột, Value = danh sách dữ liệu của cột đó
nhan_vien = pd.DataFrame({
    "Ten":       ["An",    "Bình",  "Chi",   "Duy",   "Em"],
    "Phong":     ["IT",    "Kinh doanh", "IT", "HR", "Kinh doanh"],
    "Luong":     [15000000, 20000000, 18000000, 12000000, 22000000],
    "KinhNghiem": [3,       5,        4,        2,        6]
})
print(nhan_vien)

# --- Khám phá DataFrame (EDA bước đầu) ---
# LUÔN làm những bước này ĐẦU TIÊN khi nhận dataset mới

print(nhan_vien.shape)        # (5, 4) → 5 hàng, 4 cột
print(nhan_vien.dtypes)       # kiểu dữ liệu từng cột
print(nhan_vien.info())       # kiểu dữ liệu + số non-null (phát hiện missing data)
print(nhan_vien.describe())   # thống kê nhanh: count, mean, std, min, 25%, 50%, 75%, max
print(nhan_vien.head(3))      # 3 hàng đầu
print(nhan_vien.tail(2))      # 2 hàng cuối

# --- Truy cập cột và hàng ---

# Lấy 1 cột → trả về Series
luong = nhan_vien["Luong"]
print(type(luong))   # <class 'pandas.core.series.Series'>

# Lấy nhiều cột → trả về DataFrame
# ⚠️  Chú ý: hai dấu ngoặc vuông [[ ]]
thong_tin = nhan_vien[["Ten", "Luong"]]
print(thong_tin)

# .loc[nhãn] → truy cập bằng TÊN index
print(nhan_vien.loc[0])     # hàng đầu tiên (index = 0)
print(nhan_vien.loc[2])     # hàng thứ 3 (index = 2)

# .iloc[số] → truy cập bằng VỊ TRÍ số
print(nhan_vien.iloc[0])    # hàng đầu tiên (vị trí 0)
print(nhan_vien.iloc[-1])   # hàng cuối cùng

# Truy cập ô cụ thể
print(nhan_vien.loc[1, "Luong"])   # 20000000  (Bình, cột Luong)
print(nhan_vien.iloc[1, 2])        # 20000000  (hàng 1, cột 2)


# -----------------------------------------------------------------------------
# 2.4 Đọc Dữ Liệu Thực Tế
# -----------------------------------------------------------------------------

# Đọc file CSV (phổ biến nhất)
df = pd.read_csv("data/sales.csv")

# Các tham số hay dùng:
df = pd.read_csv(
    "data/sales.csv",     
     sep=",",                #dấu phân cách, mặc định là dấu phẩy    
     encoding="utf-8",       # mã hóa ký tự (utf-8-sig cho file tiếng Việt)
     index_col=0,            # cột nào làm index (thường dùng cột ID)
     parse_dates=["NgayBan"] # chuyển cột này sang kiểu datetime tự động
 )

# Đọc file Excel
df = pd.read_excel("data/bao_cao.xlsx", sheet_name="Sheet1")

# Lưu file CSV
df.to_csv("output/ket_qua.csv", index=False)  # index=False: không lưu STT


# -----------------------------------------------------------------------------
# 2.5 Sampling — Lấy Mẫu Dữ Liệu
# -------------------------------------;''----------------------------------------

# Harvard CS109 nhấn mạnh: cách bạn lấy mẫu ảnh hưởng trực tiếp đến kết luận.
# Dataset lớn không phải lúc nào cũng cần dùng hết — và lấy mẫu sai → bias.

import pandas as pd
import numpy as np

# Giả sử có dataset 10,000 đơn hàng
np.random.seed(42)
df = pd.DataFrame({
    "MaDH":    range(101),
    "Doanh":   np.random.exponential(500000, 101).round(),
    "KhuVuc":  np.random.choice(["HCM","HN","DN","CT"], 101, p=[0.4,0.35,0.15,0.1])
})

# --- Random Sampling: lấy mẫu ngẫu nhiên ---
# Dùng khi: dataset quá lớn, muốn test nhanh
mau_200  = df.sample(n=200, random_state=42)       # lấy đúng 200 hàng
mau_5pct = df.sample(frac=0.05, random_state=42)   # lấy 5% toàn bộ

# --- Stratified Sampling: lấy mẫu theo tỉ lệ nhóm ---
# Dùng khi: muốn mẫu đại diện cho TẤT CẢ nhóm
# Ví dụ: đảm bảo HCM/HN/DN/CT đều có trong mẫu theo đúng tỉ lệ
mau_stratified = df.groupby("KhuVuc", group_keys=False).sample(
    frac=0.05,
    random_state=42
)
print(mau_stratified["KhuVuc"].value_counts(normalize=True))
# HCM    0.40   → giữ đúng tỉ lệ 40%
# HN     0.35   → giữ đúng tỉ lệ 35%
# DN     0.15   → giữ đúng tỉ lệ 15%
# CT     0.10   → giữ đúng tỉ lệ 10%

# Tại sao Stratified quan trọng hơn Random?
# Nếu random sampling "xui" bỏ sót khu vực CT (chỉ có 10%),
# mọi kết luận về CT sẽ sai.
# Stratified đảm bảo mọi nhóm đều được đại diện.

# ✏️  Tóm tắt 1 dòng: Random = nhanh;
#     Stratified = chính xác hơn khi data có nhóm không đều nhau.


# -----------------------------------------------------------------------------
# 2.6 loc và iloc — Truy Cập Nâng Cao
# -----------------------------------------------------------------------------

# Tạo DataFrame với index TÙY CHỈNH (không phải 0,1,2...)
don_hang = pd.DataFrame({
    "SanPham": ["Áo",  "Quần", "Giày",  "Túi",   "Mũ"],
    "GiaBan":  [200000, 350000, 500000, 450000, 120000],
    "SoLuong": [50,     30,     20,     15,      80],
    "DanhMuc": ["May mặc", "May mặc", "Phụ kiện", "Phụ kiện", "May mặc"]
}, index=["DH001", "DH002", "DH003", "DH004", "DH005"])  # ← index là mã đơn hàng

print(don_hang)

# --- .loc → dùng NHÃN (label) ---
print(don_hang.loc["DH003"])              # hàng DH003
print(don_hang.loc["DH001":"DH003"])      # DH001 đến DH003 (KÈM DH003)
print(don_hang.loc["DH002", "GiaBan"])    # 350000
print(don_hang.loc[:, "GiaBan"])          # cột GiaBan tất cả hàng
print(don_hang.loc[:, ["GiaBan", "SoLuong"]])  # 2 cột

# --- .iloc → dùng SỐ VỊ TRÍ (positon) ---
print(don_hang.iloc[2])                   # hàng thứ 3 (vị trí 2)
print(don_hang.iloc[0:3])                 # 3 hàng đầu (KHÔNG kèm vị trí 3)
print(don_hang.iloc[1, 1])               # 350000 (hàng 1, cột 1)
print(don_hang.iloc[:, 1])               # cột thứ 2 (GiaBan)
print(don_hang.iloc[1:4, 0:2])           # vùng con

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

# Lọc đơn giản
nv_luong_cao = nv[nv["Luong"] > 17]
nv_IT = nv[nv["Phong"] == "IT"]

# Lọc nhiều điều kiện
# ⚠️  Dùng & (và), | (hoặc), ~ (phủ định) — KHÔNG dùng and/or
# ⚠️  PHẢI có ngoặc () quanh mỗi điều kiện

nv_IT_cao    = nv[(nv["Phong"] == "IT") & (nv["Luong"] > 15)]   # IT VÀ lương >15
nv_KD_HR     = nv[(nv["Phong"] == "KD") | (nv["Phong"] == "HR")]# KD HOẶC HR
nv_khong_IT  = nv[~(nv["Phong"] == "IT")]                        # KHÔNG phải IT

# isin() → lọc nhiều giá trị cùng lúc
nv_KD_HR_v2 = nv[nv["Phong"].isin(["KD", "HR"])]   # gọn hơn

# between() → lọc khoảng giá trị
nv_luong_tb = nv[nv["Luong"].between(15, 20)]       # 15 ≤ Luong ≤ 20

# str.contains() → lọc string
san_pham = pd.DataFrame({"Ten": ["Áo thun", "Áo khoác", "Quần jeans", "Áo polo"]})
ao = san_pham[san_pham["Ten"].str.contains("Áo")]
print(ao)


# -----------------------------------------------------------------------------
# 2.8 Thêm, Sửa, Xóa Cột
# -----------------------------------------------------------------------------

nv = pd.DataFrame({
    "Ten":   ["An", "Bình", "Chi", "Duy"],
    "Luong": [15, 20, 18, 12],
    "Phong": ["IT", "KD", "IT", "HR"]
})

# Thêm cột mới
nv["Thue"]     = nv["Luong"] * 0.1          # thuế 10%
nv["ThucNhan"] = nv["Luong"] - nv["Thue"]   # lương thực nhận
nv["Cap"]      = "Nhân viên"                 # giá trị cố định cho tất cả

# Sửa giá trị
nv["Phong"] = nv["Phong"].replace({"KD": "Kinh doanh", "HR": "Nhân sự"})
nv.loc[nv["Ten"] == "An", "Luong"] = 17     # tăng lương An lên 17

# Xóa cột
nv = nv.drop(columns=["Thue"])              # xóa cột Thue

# Xóa hàng
nv = nv.drop(index=2)                       # xóa hàng có index = 2
# Đổi tên cột
nv = nv.rename(columns={"Ten": "HoTen", "Luong": "LuongCoBan"})
print(nv)


# -----------------------------------------------------------------------------
# 2.9 Xử Lý Dữ Liệu Thiếu (Missing Data)
# -----------------------------------------------------------------------------

# Đây là kỹ năng KHÔNG THỂ THIẾU — dữ liệu thực tế luôn có lỗ hổng.

import pandas as pd
import numpy as np

# Dataset có missing values (NaN = Not a Number)
df = pd.DataFrame({
    "Ten":    ["An", "Bình", None,   "Duy",    "Em"],
    "Tuoi":   [25,    np.nan, 28,    30,        np.nan],
    "Luong":  [15000, 20000,  18000, np.nan,    22000],
    "Kinh":   [3,     5,      4,     2,         6]
})
print(df)

# Phát hiện missing data
print(df.isnull())                         # True = bị thiếu
print(df.isnull().sum())                   # Đếm số NaN mỗi cột
print(df.isnull().sum() / len(df) * 100)   # % thiếu mỗi cột

# Xóa hàng có NaN
df_sach  = df.dropna()                     # xóa hàng có BẤT KỲ NaN nào
df_sach2 = df.dropna(subset=["Luong"])     # chỉ xóa nếu cột Luong bị NaN
df_sach3 = df.dropna(thresh=3)            # giữ hàng có ít nhất 3 giá trị non-NaN

# Điền giá trị vào chỗ thiếu
df["Ten"]   = df["Ten"].fillna("Không rõ")

tb_tuoi     = df["Tuoi"].mean()
df["Tuoi"]  = df["Tuoi"].fillna(tb_tuoi)   # điền bằng trung bình

tv_luong    = df["Luong"].median()
df["Luong"] = df["Luong"].fillna(tv_luong)  # điền bằng trung vị (tốt hơn khi có outliers)

# Điền forward fill (tốt cho dữ liệu chuỗi thời gian)
# df["Luong"] = df["Luong"].fillna(method="ffill")

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

nv = pd.DataFrame({
    "Ten":   ["An", "Bình", "Chi", "Duy", "Em", "Phúc", "Giang"],
    "Phong": ["IT", "KD",   "IT",  "HR",  "KD", "IT",   "HR"],
    "Luong": [15,   20,     18,    12,    22,   16,     14],
    "Nam":   [3,    5,      4,     2,     6,    1,      3]
})

# GroupBy cơ bản: "Tính trung bình lương theo từng phòng"
theo_phong = nv.groupby("Phong")["Luong"].mean()
print(theo_phong)
# HR    13.0
# IT    16.33...
# KD    21.0

# Nhiều hàm tổng hợp cùng lúc
tong_hop = nv.groupby("Phong")["Luong"].agg(["mean", "sum", "count", "max"])
print(tong_hop)

# Nhiều cột cùng lúc
ket_qua = nv.groupby("Phong").agg({
    "Luong": ["mean", "max"],   # mean và max của Luong
    "Nam":   "mean"             # mean của Nam
})
print(ket_qua)

# reset_index: chuyển kết quả GroupBy thành DataFrame bình thường
theo_phong_df = nv.groupby("Phong")["Luong"].mean().reset_index()
print(theo_phong_df)

# GroupBy theo nhiều cột
df_ban_hang = pd.DataFrame({
    "Thang": [1,1,2,2,1,2],
    "SP":    ["A","B","A","B","A","B"],
    "Doanh": [100,200,150,180,120,220]
})
tong_thang_sp = df_ban_hang.groupby(["Thang", "SP"])["Doanh"].sum()
print(tong_thang_sp)

# ✏️  Tóm tắt 1 dòng: groupby("cột")["cột_khác"].hàm() = tính hàm đó cho từng nhóm.


# -----------------------------------------------------------------------------
# 2.11 Apply & Map — Biến Đổi Dữ Liệu
# -----------------------------------------------------------------------------

# --- map() — Áp dụng trên từng phần tử của Series ---

df = pd.DataFrame({
    "Ten":  ["An", "Bình", "Chi", "Duy"],
    "Diem": [8.5, 6.5, 9.0, 5.0]
})

# Dùng dict để map giá trị
xep_loai_dict = {8.5: "Giỏi", 6.5: "Khá", 9.0: "Xuất sắc", 5.0: "Trung bình"}
df["XepLoai"] = df["Diem"].map(xep_loai_dict)

# Dùng hàm lambda để tính toán
df["Diem100"] = df["Diem"].map(lambda d: d * 10)  # chuyển sang thang 100

# --- apply() — Áp dụng hàm phức tạp hơn ---

df = pd.DataFrame({
    "Ten":   ["An", "Bình", "Chi", "Duy"],
    "Luong": [15,   20,     18,    12],   # triệu
    "Nam":   [3,    5,      4,     2]
})

# apply trên 1 cột
def xep_cap(luong):
    if luong >= 20:
        return "Senior"
    elif luong >= 15:
        return "Mid"
    else:
        return "Junior"

df["Cap"] = df["Luong"].apply(xep_cap)
print(df)

# apply trên nhiều cột (axis=1: đọc từng hàng)
def luong_thuc_nhan(hang):
    if hang["Nam"] >= 5:
        bonus = hang["Luong"] * 0.15   # bonus 15%
    else:
        bonus = hang["Luong"] * 0.05   # bonus 5%
    return hang["Luong"] + bonus

df["LuongTN"] = df.apply(luong_thuc_nhan, axis=1)
print(df)


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

# inner join: chỉ giữ hàng KHỚP ở CẢ 2 bảng (mặc định)
ket_qua = pd.merge(don_hang, khach_hang, on="MaKH", how="inner")
print(ket_qua)

# left join: giữ TẤT CẢ hàng của bảng TRÁI
ket_qua_left = pd.merge(don_hang, khach_hang, on="MaKH", how="left")

# concat: ghép theo chiều dọc (nối thêm hàng)
thang1 = pd.DataFrame({"SP": ["A","B"], "Doanh": [100, 200]})
thang2 = pd.DataFrame({"SP": ["A","C"], "Doanh": [150, 180]})
tat_ca = pd.concat([thang1, thang2], ignore_index=True)
print(tat_ca)


# -----------------------------------------------------------------------------
# 2.13 Xử Lý Thời Gian (DateTime)
# -----------------------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "NgayBan": ["2024-01-15", "2024-02-20", "2024-03-05"],
    "Doanh":   [500000,       750000,        300000]
})

# Chuyển string thành datetime
df["NgayBan"] = pd.to_datetime(df["NgayBan"])
print(df.dtypes)  # NgayBan: datetime64[ns]

# Trích xuất thành phần thời gian
df["Nam"]          = df["NgayBan"].dt.year
df["Thang"]        = df["NgayBan"].dt.month
df["Ngay"]         = df["NgayBan"].dt.day
df["ThuTrongTuan"] = df["NgayBan"].dt.day_name()   # "Monday", "Tuesday"...
print(df)

# Lọc theo khoảng thời gian
q1_2024 = df[(df["NgayBan"] >= "2024-01-01") & (df["NgayBan"] < "2024-04-01")]

# Groupby theo tháng
theo_thang = df.groupby(df["NgayBan"].dt.month)["Doanh"].sum()


# -----------------------------------------------------------------------------
# 2.14 Các Hàm Tiện Ích Hay Dùng
# -----------------------------------------------------------------------------

df = pd.DataFrame({
    "SP":     ["Áo", "Quần", "Áo", "Giày", "Quần", "Áo"],
    "Doanh":  [200, 350, 220, 500, 400, 180],
    "Phong":  ["HCM","HN","HCM","DN","HN","HCM"]
})

# value_counts() → đếm số lần xuất hiện của mỗi giá trị
print(df["SP"].value_counts())
# Áo      3, Quần    2, Giày    1

# unique() và nunique() → các giá trị duy nhất
print(df["SP"].unique())    # ['Áo' 'Quần' 'Giày']
print(df["SP"].nunique())   # 3

# sort_values() → sắp xếp
df_sorted = df.sort_values("Doanh", ascending=False)  # giảm dần
df_multi  = df.sort_values(["Phong", "Doanh"])         # nhiều cột

# duplicated() và drop_duplicates()
print(df.duplicated())
df_sach = df.drop_duplicates()

# cut() → chia giá trị liên tục thành nhóm (bins)
diem = pd.Series([5, 6.5, 7, 8, 8.5, 9, 4, 7.5])
nhan = pd.cut(diem,
              bins=[0, 5, 6.5, 8, 10],
              labels=["Yếu", "Trung bình", "Khá", "Giỏi"])
print(nhan)

# pivot_table() → bảng tổng hợp như Excel PivotTable
pivot = pd.pivot_table(df,
                       values="Doanh",
                       index="Phong",
                       columns="SP",
                       aggfunc="sum",
                       fill_value=0)
print(pivot)


# =============================================================================
# PHẦN 3: SCIPY.STATS — STATISTICAL TESTING
# =============================================================================

# Harvard CS109: "visualize thôi chưa đủ — phải kiểm định thống kê
# để biết kết quả có thực sự ý nghĩa không."
# Đây là điểm phân biệt Data Scientist với người chỉ biết vẽ biểu đồ.

# 3 khái niệm cốt lõi:
# ─ p-value: xác suất quan sát kết quả này nếu thực tế KHÔNG có sự khác biệt
#   p < 0.05  → sự khác biệt có ý nghĩa thống kê
#   p ≥ 0.05  → chưa đủ bằng chứng, có thể là ngẫu nhiên
# ─ H₀ (Null):        "không có gì đặc biệt" (2 nhóm có cùng trung bình)
# ─ H₁ (Alternative): điều bạn muốn chứng minh (nhóm A cao hơn nhóm B)


# -----------------------------------------------------------------------------
# 3.3 t-test — So Sánh 2 Nhóm
# -----------------------------------------------------------------------------

from scipy import stats
import numpy as np
import pandas as pd

# Ví dụ thực tế: A/B test website
np.random.seed(42)
doanh_thu_A = np.random.normal(loc=2.0, scale=0.5, size=50)  # triệu/người
doanh_thu_B = np.random.normal(loc=2.3, scale=0.5, size=50)  # nhóm B cao hơn

print(f"Trung bình nhóm A: {doanh_thu_A.mean():.3f} triệu")
print(f"Trung bình nhóm B: {doanh_thu_B.mean():.3f} triệu")
print(f"Chênh lệch: {doanh_thu_B.mean() - doanh_thu_A.mean():.3f} triệu")

# Independent t-test: so sánh 2 nhóm ĐỘC LẬP
t_stat, p_value = stats.ttest_ind(doanh_thu_A, doanh_thu_B)

print(f"\nt-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("→ Sự khác biệt CÓ Ý NGHĨA thống kê (p < 0.05)")
    print("→ Trang web mới THỰC SỰ tốt hơn, không phải may mắn")
else:
    print("→ Chưa đủ bằng chứng (p ≥ 0.05)")
    print("→ Sự khác biệt có thể chỉ là ngẫu nhiên")

# Paired t-test: so sánh CÙNG 1 đối tượng trước/sau
doanh_so_truoc = np.array([15, 18, 12, 20, 16, 14, 22, 19])
doanh_so_sau   = np.array([18, 20, 15, 22, 18, 17, 24, 21])

t2, p2 = stats.ttest_rel(doanh_so_truoc, doanh_so_sau)
print(f"\nPaired t-test p-value: {p2:.4f}")
if p2 < 0.05:
    print("→ Training CÓ hiệu quả thống kê")


# -----------------------------------------------------------------------------
# 3.4 Pearson Correlation — Kiểm Định Mối Quan Hệ
# -----------------------------------------------------------------------------

np.random.seed(42)
kinh_nghiem = np.random.randint(1, 15, 50)
luong = kinh_nghiem * 1.5 + np.random.randn(50) * 2 + 10

# r gần  1: tương quan dương mạnh
# r gần -1: tương quan âm mạnh
# r gần  0: không tương quan
r, p_value = stats.pearsonr(kinh_nghiem, luong)

print(f"Hệ số tương quan (r): {r:.4f}")
print(f"p-value: {p_value:.6f}")

if p_value < 0.05:
    print(f"→ Tương quan r={r:.2f} có ý nghĩa thống kê")
    if r > 0.7:
        print("→ Tương quan MẠNH: kinh nghiệm nhiều → lương cao")
    elif r > 0.3:
        print("→ Tương quan VỪA")
    else:
        print("→ Tương quan YẾU dù có ý nghĩa")
else:
    print("→ Tương quan chưa đủ bằng chứng thống kê")


# -----------------------------------------------------------------------------
# 3.5 Normality Test — Kiểm Tra Phân Phối Chuẩn
# -----------------------------------------------------------------------------

# Nhiều statistical test giả định dữ liệu có phân phối chuẩn.
# Cần kiểm tra trước.

data_chuan = np.random.normal(0, 1, 100)    # phân phối chuẩn
data_lech  = np.random.exponential(1, 100)  # phân phối lệch

# Shapiro-Wilk test (tốt cho n < 2000)
# H₀: dữ liệu có phân phối chuẩn
stat1, p1 = stats.shapiro(data_chuan)
stat2, p2 = stats.shapiro(data_lech)

print(f"Data chuẩn  → p={p1:.4f}", "✅ Chuẩn" if p1 > 0.05 else "❌ Không chuẩn")
print(f"Data lệch   → p={p2:.4f}", "✅ Chuẩn" if p2 > 0.05 else "❌ Không chuẩn")

# Nếu không chuẩn → dùng Mann-Whitney U test thay cho t-test
stat_mw, p_mw = stats.mannwhitneyu(data_chuan, data_lech, alternative="two-sided")
print(f"\nMann-Whitney p-value: {p_mw:.6f}")

# Quy trình kiểm định (Harvard CS109 approach):
# 1. Đặt câu hỏi cụ thể ("Nhóm A có tốt hơn B không?")
# 2. Visualize trước (histogram, boxplot)
# 3. Kiểm tra phân phối (Shapiro-Wilk)
# 4. Chọn test phù hợp (t-test nếu chuẩn, Mann-Whitney nếu không)
# 5. Diễn giải p-value trong ngữ cảnh bài toán


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

fig, ax = plt.subplots(figsize=(8, 5))  # rộng 8 inch, cao 5 inch

thang     = [1, 2, 3, 4, 5, 6]
doanh_thu = [150, 200, 180, 250, 300, 280]

ax.plot(thang, doanh_thu,
        color="steelblue",    # màu đường
        marker="o",           # điểm tròn tại mỗi giá trị
        linewidth=2,          # độ dày đường
        label="Doanh thu")    # nhãn cho legend

ax.set_title("Doanh Thu 6 Tháng Đầu Năm", fontsize=14, fontweight="bold")
ax.set_xlabel("Tháng")
ax.set_ylabel("Triệu đồng")
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("bieu_do.png", dpi=150, bbox_inches="tight")  # lưu file
plt.show()

# --- Bar Chart — So Sánh Các Nhóm ---

phong    = ["IT", "Kinh doanh", "HR", "Marketing"]
luong_tb = [18.5, 21.0, 13.5, 16.0]   # triệu đồng

fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(phong, luong_tb,
              color=["#2196F3", "#FF5722", "#4CAF50", "#FF9800"],
              edgecolor="white",
              width=0.6)

# Thêm số lên đầu mỗi cột
for bar, val in zip(bars, luong_tb):
    ax.text(bar.get_x() + bar.get_width()/2,  # x: giữa cột
            bar.get_height() + 0.2,           # y: trên đỉnh cột
            f"{val:.1f}",                     # text
            ha="center", va="bottom",
            fontweight="bold")

ax.set_title("Lương Trung Bình Theo Phòng Ban")
ax.set_ylabel("Lương (triệu đồng)")
ax.set_ylim(0, 25)
plt.tight_layout()
plt.show()

# --- Histogram — Phân Phối Dữ Liệu ---

np.random.seed(42)
diem_thi = np.random.normal(loc=7.0, scale=1.5, size=200)
diem_thi = np.clip(diem_thi, 0, 10)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(diem_thi, bins=20, color="steelblue", edgecolor="white", alpha=0.8)

ax.axvline(diem_thi.mean(),      color="red",    linestyle="--",
           label=f"Trung bình: {diem_thi.mean():.2f}")
ax.axvline(np.median(diem_thi),  color="orange", linestyle="-.",
           label=f"Trung vị: {np.median(diem_thi):.2f}")

ax.set_title("Phân Phối Điểm Thi")
ax.set_xlabel("Điểm")
ax.set_ylabel("Số học sinh")
ax.legend()
plt.tight_layout()
plt.show()

# --- Scatter Plot — Mối Quan Hệ Giữa 2 Biến ---

np.random.seed(42)
n = 100
kinh_nghiem = np.random.randint(1, 15, n)
luong = kinh_nghiem * 2 + np.random.randn(n) * 3 + 8

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(kinh_nghiem, luong, color="steelblue", alpha=0.6, edgecolors="white", s=60)

# Thêm đường xu hướng (trend line)
z      = np.polyfit(kinh_nghiem, luong, 1)
p      = np.poly1d(z)
x_line = np.linspace(1, 15, 100)
ax.plot(x_line, p(x_line), color="red", linewidth=2, label="Xu hướng")

ax.set_title("Mối Quan Hệ Kinh Nghiệm & Lương")
ax.set_xlabel("Kinh nghiệm (năm)")
ax.set_ylabel("Lương (triệu đồng)")
ax.legend()
plt.tight_layout()
plt.show()

# --- Subplots — Nhiều Biểu Đồ Cùng Lúc ---

fig, axes = plt.subplots(2, 2, figsize=(12, 8))  # 2 hàng, 2 cột
# axes là mảng 2D: axes[0,0], axes[0,1], axes[1,0], axes[1,1]

axes[0, 0].plot([1,2,3,4], [10,20,15,25])
axes[0, 0].set_title("Biểu đồ 1")

axes[0, 1].bar(["A","B","C"], [30, 50, 40])
axes[0, 1].set_title("Biểu đồ 2")

axes[1, 0].hist(np.random.randn(200), bins=20)
axes[1, 0].set_title("Biểu đồ 3")

axes[1, 1].scatter(np.random.rand(50), np.random.rand(50))
axes[1, 1].set_title("Biểu đồ 4")

plt.suptitle("Dashboard Tổng Hợp", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.show()


# -----------------------------------------------------------------------------
# 4.3 Seaborn — Đẹp Hơn, Dễ Hơn
# -----------------------------------------------------------------------------

import seaborn as sns

sns.set_theme(style="whitegrid")   # nền trắng có lưới (khuyến nghị)
# style khác: "darkgrid", "white", "dark", "ticks"

# Tạo dataset mẫu
np.random.seed(42)
df = pd.DataFrame({
    "Phong":    np.random.choice(["IT", "KD", "HR"], 100),
    "Luong":    np.random.normal(18, 4, 100).round(1),
    "Nam":      np.random.randint(1, 10, 100),
    "GioiTinh": np.random.choice(["Nam", "Nữ"], 100)
})

# --- 1. Histogram + KDE (phân phối) ---
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data=df, x="Luong", kde=True, bins=20, color="steelblue", ax=ax)
ax.set_title("Phân Phối Lương")
plt.show()

# --- 2. Boxplot (phân phối theo nhóm) ---
# Cho thấy: trung vị, Q1, Q3, outliers
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x="Phong", y="Luong", palette="Set2", ax=ax)
ax.set_title("Phân Phối Lương Theo Phòng")
plt.show()

# --- 3. Barplot (trung bình theo nhóm) ---
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=df, x="Phong", y="Luong",
            hue="GioiTinh",   # chia thêm theo giới tính
            palette="coolwarm",
            errorbar="sd",    # thanh sai số = độ lệch chuẩn
            ax=ax)
ax.set_title("Lương Trung Bình Theo Phòng & Giới Tính")
plt.show()

# --- 4. Scatterplot ---
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df, x="Nam", y="Luong",
                hue="Phong",    # màu theo phòng
                style="Phong",  # hình theo phòng
                s=80, ax=ax)
ax.set_title("Kinh Nghiệm vs Lương")
plt.show()

# --- 5. Heatmap — Tương Quan Giữa Các Biến ---
corr_matrix = df[["Luong", "Nam"]].corr()

fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(corr_matrix,
            annot=True,       # hiện số trong ô
            fmt=".2f",        # 2 chữ số thập phân
            cmap="coolwarm",  # đỏ=tương quan dương, xanh=âm
            vmin=-1, vmax=1,
            ax=ax)
ax.set_title("Ma Trận Tương Quan")
plt.show()

# --- 6. Pairplot — Tương Quan Tất Cả Các Biến ---
# Dùng khi muốn cái nhìn tổng quan về dataset
sns.pairplot(df[["Luong", "Nam"]], diag_kind="kde")
plt.suptitle("Pairplot", y=1.02)
plt.show()


# =============================================================================
# PHẦN 5: WORKFLOW THỰC TẾ — EDA (Harvard CS109 Style)
# =============================================================================

# Harvard CS109 nhấn mạnh:
# "EDA không phải là 'nhìn vào data rồi xem có gì'.
#  EDA là đặt câu hỏi cụ thể trước, rồi dùng data để trả lời."
#
# Trước khi mở notebook, hãy viết ra ít nhất 3–5 câu hỏi:
#   1. Phòng nào trả lương cao nhất? Thấp nhất?
#   2. Kinh nghiệm có thực sự tương quan với lương không?
#   3. Tỉ lệ nam/nữ theo phòng ban như thế nào?
#   4. Nhân viên nghỉ việc (churn) tập trung ở nhóm nào?
#   5. Lương phân phối như thế nào — chuẩn hay lệch?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_theme(style="whitegrid")

# ─── BƯỚC 1: ĐỌC & NHÌN TỔNG QUAN ──────────────────────────────────────────
# df = pd.read_csv("data.csv")   # ← thay bằng file thực tế của bạn

# Demo với dữ liệu giả:
np.random.seed(42)
df = pd.DataFrame({
    "Luong":  np.random.normal(18, 4, 100).round(1),
    "Nam":    np.random.randint(1, 10, 100),
    "Phong":  np.random.choice(["IT", "KD", "HR"], 100),
    "GioiTinh": np.random.choice(["Nam", "Nữ"], 100)
})

print("=== THÔNG TIN CƠ BẢN ===")
print(f"Kích thước: {df.shape[0]:,} hàng × {df.shape[1]} cột")
print(f"\nKiểu dữ liệu:\n{df.dtypes}")
print(f"\n5 hàng đầu:\n{df.head()}")

# ─── BƯỚC 2: KIỂM TRA CHẤT LƯỢNG DỮ LIỆU ───────────────────────────────────
print("\n=== MISSING DATA ===")
missing     = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_report = pd.DataFrame({
    "Số lượng NaN":  missing,
    "Phần trăm (%)": missing_pct
}).query("`Số lượng NaN` > 0").sort_values("Phần trăm (%)", ascending=False)
print(missing_report if len(missing_report) > 0 else "Không có missing data ✅")

print("\n=== DUPLICATE ROWS ===")
n_dup = df.duplicated().sum()
print(f"Số hàng trùng lặp: {n_dup} ({n_dup/len(df)*100:.2f}%)")

# ─── BƯỚC 3: THỐNG KÊ MÔ TẢ ─────────────────────────────────────────────────
print("\n=== THỐNG KÊ MÔ TẢ ===")
print(df.describe().T.round(2))   # .T để xoay cho dễ đọc

# ─── BƯỚC 4: ĐẶT CÂU HỎI → VẼ BIỂU ĐỒ ─────────────────────────────────────

so_cols  = df.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = df.select_dtypes(include=["object"]).columns.tolist()

# Câu hỏi 1: Phân phối từng biến số trông như thế nào?
n = len(so_cols)
if n > 0:
    fig, axes = plt.subplots(1, n, figsize=(5*n, 4))
    if n == 1: axes = [axes]
    for ax, col in zip(axes, so_cols):
        sns.histplot(df[col].dropna(), kde=True, ax=ax, color="steelblue")
        ax.set_title(f"{col}")
        ax.axvline(df[col].mean(),   color="red",    ls="--", lw=1.5, label="Mean")
        ax.axvline(df[col].median(), color="orange", ls="-.", lw=1.5, label="Median")
        ax.legend(fontsize=8)
    plt.suptitle("Phân Phối Các Biến Số", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

# Câu hỏi 2: Có outliers không?
if n > 0:
    fig, axes = plt.subplots(1, n, figsize=(4*n, 4))
    if n == 1: axes = [axes]
    for ax, col in zip(axes, so_cols):
        sns.boxplot(y=df[col].dropna(), ax=ax, color="lightblue",
                    flierprops=dict(marker="o", color="red", alpha=0.5))
        ax.set_title(f"{col}")
    plt.suptitle("Phát Hiện Outliers", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

# Câu hỏi 3: Các biến số tương quan với nhau thế nào?
if n >= 2:
    corr = df[so_cols].corr()
    fig, ax = plt.subplots(figsize=(max(6, n*1.5), max(5, n*1.2)))
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
                vmin=-1, vmax=1, mask=mask, ax=ax, annot_kws={"size": 10})
    ax.set_title("Ma Trận Tương Quan", fontsize=14)
    plt.tight_layout()
    plt.show()

    corr_pairs = (corr.where(~mask)
                      .stack()
                      .reset_index()
                      .rename(columns={0: "r", "level_0": "Biến 1", "level_1": "Biến 2"})
                      .sort_values("r", key=abs, ascending=False))
    print("\nTop 5 cặp tương quan mạnh nhất:")
    print(corr_pairs.head())

# Câu hỏi 4: Biến phân loại phân bổ thế nào?
for col in cat_cols[:3]:
    vc = df[col].value_counts()
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=vc.index, y=vc.values, palette="Set2", ax=ax)
    ax.set_title(f"Phân Bổ: {col}")
    ax.set_ylabel("Số lượng")
    for bar, val in zip(ax.patches, vc.values):
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() + 0.5,
                f"{val:,}", ha="center", fontsize=9)
    plt.tight_layout()
    plt.show()

# Câu hỏi 5: So sánh nhóm (biến số + biến phân loại)
if len(so_cols) > 0 and len(cat_cols) > 0:
    target_num = so_cols[0]
    target_cat = cat_cols[0]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    sns.boxplot(data=df, x=target_cat, y=target_num, palette="Set2", ax=ax1)
    ax1.set_title(f"{target_num} theo {target_cat}")

    sns.barplot(data=df, x=target_cat, y=target_num,
                palette="Set2", errorbar="ci", ax=ax2)
    ax2.set_title(f"Trung bình {target_num} theo {target_cat}")
    plt.tight_layout()
    plt.show()

    nhom_list = df[target_cat].dropna().unique()
    if len(nhom_list) == 2:
        g1 = df[df[target_cat] == nhom_list[0]][target_num].dropna()
        g2 = df[df[target_cat] == nhom_list[1]][target_num].dropna()
        t, p = stats.ttest_ind(g1, g2)
        print(f"\nT-test [{nhom_list[0]} vs {nhom_list[1]}]: p={p:.4f}",
              "→ Có ý nghĩa ✅" if p < 0.05 else "→ Không có ý nghĩa")
    else:
        nhom_data = [df[df[target_cat]==g][target_num].dropna() for g in nhom_list]
        f, p = stats.f_oneway(*nhom_data)
        print(f"\nANOVA ({target_cat}): p={p:.4f}",
              "→ Ít nhất 1 nhóm khác biệt ✅" if p < 0.05 else "→ Các nhóm tương đương")

# ─── BƯỚC 5: TÓM TẮT INSIGHTS ────────────────────────────────────────────────
print("\n" + "="*60)
print("INSIGHTS TÓM TẮT")
print("="*60)
print(f"Dataset: {df.shape[0]:,} quan sát, {df.shape[1]} biến")
print(f"Missing: {df.isnull().sum().sum()} ô ({df.isnull().mean().mean()*100:.1f}%)")
print("\n→ Ghi chú các câu hỏi chưa có câu trả lời để điều tra tiếp.")


# =============================================================================
# PHẦN 6: DATA STORYTELLING — COMMUNICATION
# =============================================================================

# Harvard CS109: "Kết quả tốt mà communicate kém = không ai dùng."
#
# Nguyên tắc:
# 1. Mỗi biểu đồ phải trả lời ĐÚNG 1 câu hỏi
# 2. Tiêu đề phải là KẾT LUẬN, không chỉ là tên biến
#    ❌ "Scatter plot of Experience vs Salary"
#    ✅ "Kinh Nghiệm Nhiều Hơn → Lương Cao Hơn (r=0.78)"
# 3. Highlight điểm quan trọng nhất
# 4. Bỏ tất cả thứ không cần thiết (chartjunk)

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sns.set_theme(style="white")  # nền trắng, không lưới → sạch hơn

np.random.seed(42)
df = pd.DataFrame({
    "Phong":  ["IT"]*30 + ["KD"]*30 + ["HR"]*20,
    "Luong":  np.concatenate([
        np.random.normal(18, 3, 30),
        np.random.normal(22, 4, 30),
        np.random.normal(13, 2, 20)
    ]),
    "Nam": np.random.randint(1, 10, 80)
})

# --- Ví dụ 1: Tiêu đề là insight, không phải tên biến ---
fig, ax = plt.subplots(figsize=(9, 5))

order   = df.groupby("Phong")["Luong"].median().sort_values(ascending=False).index
palette = {"KD": "#e74c3c", "IT": "#3498db", "HR": "#95a5a6"}

sns.boxplot(data=df, x="Phong", y="Luong", order=order,
            palette=palette, width=0.5, ax=ax)

# Highlight nhóm cao nhất
ax.patches[0].set_edgecolor("#c0392b")
ax.patches[0].set_linewidth(2.5)

# Tiêu đề = kết luận
ax.set_title("Kinh Doanh trả lương cao nhất, HR thấp nhất",
             fontsize=13, fontweight="bold", pad=12)
ax.set_xlabel("")
ax.set_ylabel("Lương (triệu đồng)")

# Thêm median label
for i, phong in enumerate(order):
    med = df[df["Phong"]==phong]["Luong"].median()
    ax.text(i, med + 0.3, f"TB: {med:.1f}M",
            ha="center", fontsize=9, fontweight="bold")

sns.despine()
plt.tight_layout()
plt.show()

# --- Ví dụ 2: Annotate điểm đặc biệt ---
fig, ax = plt.subplots(figsize=(8, 5))

sns.scatterplot(data=df, x="Nam", y="Luong", hue="Phong",
                palette=palette, alpha=0.7, s=70, ax=ax)

# Highlight outlier
outlier = df.nlargest(1, "Luong").iloc[0]
ax.annotate(f"Outlier: {outlier['Luong']:.1f}M\n({outlier['Phong']}, {outlier['Nam']} năm)",
            xy=(outlier["Nam"], outlijer["Luong"]),
            xytext=(outlier["Nam"]-2, outlier["Luong"]-3),
            arrowprops=dict(arrowstyle="->", color="black"),
            fontsize=9, color="black",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

ax.set_title("Lương Tăng Theo Kinh Nghiệm — Ngoại Lệ Ở Kinh Doanh",
             fontsize=12, fontweight="bold")
ax.set_xlabel("Số năm kinh nghiệm")
ax.set_ylabel("Lương (triệu đồng)")
sns.despine()
plt.tight_layout()
plt.show()


# =============================================================================
# CHEAT SHEET — TÓM TẮT NHANH
# =============================================================================

# ── NumPy ────────────────────────────────────────────────────────────────────
# np.array([1,2,3])           → tạo array
# np.zeros(n), np.ones(n)     → array 0 / 1
# np.arange(start, stop, step)→ dãy số
# np.linspace(a, b, n)        → chia đều n điểm
# np.mean(), np.std(), np.sum()→ thống kê
# arr[arr > 5]                → lọc điều kiện
# arr.shape, arr.reshape(r,c) → hình dạng

# ── Pandas ───────────────────────────────────────────────────────────────────
# pd.read_csv("file.csv")                        → đọc CSV
# .head(), .info(), .describe()                  → xem nhanh
# df.sample(n=100)                               → lấy mẫu ngẫu nhiên
# df.groupby("col").apply(lambda x: x.sample())  → stratified sampling
# df[df["cot"] > 5]                              → lọc hàng
# df[(dk1) & (dk2)]                              → lọc nhiều điều kiện
# df.loc[hang, cot]                              → truy cập theo tên
# df.iloc[hang, cot]                             → truy cập theo vị trí
# df.groupby("cot")["cot2"].mean()               → nhóm & tổng hợp
# .isnull(), .fillna(), .dropna()                → missing data
# pd.merge(df1, df2, on="key")                   → ghép bảng
# df["cot_moi"] = ...                            → thêm cột
# df.sort_values("cot")                          → sắp xếp
# df["cot"].value_counts()                       → đếm giá trị

# ── Scipy.stats ──────────────────────────────────────────────────────────────
# stats.ttest_ind(g1, g2)            → so sánh 2 nhóm độc lập
# stats.ttest_rel(truoc, sau)        → so sánh trước/sau (cùng đối tượng)
# stats.pearsonr(x, y)  → (r, p)    → kiểm tra tương quan
# stats.shapiro(data)   → (stat, p) → kiểm tra phân phối chuẩn
# stats.mannwhitneyu(g1, g2)         → so sánh 2 nhóm (không chuẩn)
# stats.f_oneway(g1, g2, g3)         → so sánh >2 nhóm (ANOVA)
# → Đọc kết quả: p < 0.05 = có ý nghĩa thống kê ✅

# ── Biểu Đồ ─────────────────────────────────────────────────────────────────
# ax.plot(x, y)              → Line plot    | xu hướng theo thời gian
# sns.barplot()              → Bar chart    | so sánh các nhóm
# sns.histplot(kde=True)     → Histogram    | phân phối 1 biến
# sns.scatterplot()          → Scatter      | mối quan hệ 2 biến
# sns.boxplot()              → Boxplot      | phân phối + outliers theo nhóm
# sns.heatmap(corr, annot=True)→ Heatmap   | ma trận tương quan

# ── EDA Checklist (Harvard CS109) ────────────────────────────────────────────
# □ 1. Đặt ít nhất 3 câu hỏi cụ thể trước khi mở notebook
# □ 2. Kiểm tra shape, dtypes, head()
# □ 3. Báo cáo missing data (count + %)
# □ 4. Kiểm tra duplicates
# □ 5. describe() → nhìn mean/std/min/max
# □ 6. Histplot mỗi biến số → phân phối lệch không?
# □ 7. Boxplot → outliers ở đâu?
# □ 8. Heatmap tương quan → cặp nào đáng chú ý?
# □ 9. value_counts() mỗi biến phân loại
# □ 10. Statistical test cho câu hỏi so sánh nhóm
# □ 11. Viết insights: "Phát hiện X, cần điều tra thêm Y"

# ─────────────────────────────────────────────────────────────────────────────
# Bước tiếp theo: lấy dataset thực từ Kaggle (kaggle.com/datasets)
# hoặc UCI ML Repository (archive.ics.uci.edu), chạy EDA Workflow ở Phần 5.
# Học qua tay bao giờ cũng nhanh hơn đọc!
# ─────────────────────────────────────────────────────────────────────────────
