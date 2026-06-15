# =============================================================================
# 🤖 MACHINE LEARNING VỚI PYTHON
# Tài liệu học hoàn chỉnh từ nền tảng đến thực chiến
# =============================================================================
#
# 📚 Nguồn tham khảo chính:
#   - Stanford CS229  — Machine Learning (Andrew Ng)
#   - Harvard CS109   — Introduction to Data Science with Python
#   - Hands-On ML     — Aurélien Géron, 3rd Ed. (O'Reilly 2022)
#   - ISL             — James, Witten, Hastie, Tibshirani (statlearning.com)
#   - scikit-learn    — scikit-learn.org
#
# 💡 Yêu cầu trước khi học file này:
#    Đã học xong NumPy, Pandas, Matplotlib/Seaborn, EDA workflow cơ bản.
#
# 💻 Cách dùng trong VS Code:
#    - Cài extension "Python" của Microsoft
#    - Nhấn "Run Cell" (▶) hoặc Shift+Enter để chạy từng cell
#    - Hoặc chạy toàn bộ: python machine_learning.py
# =============================================================================

# %% [markdown]
# ## MỤC LỤC
#
# PHẦN 1  — TỔNG QUAN MACHINE LEARNING
#   1.1  ML là gì? Tại sao quan trọng?
#   1.2  Ba loại ML: Supervised / Unsupervised / Reinforcement
#   1.3  End-to-End ML Workflow
#   1.4  Overfitting, Underfitting & Bias-Variance Tradeoff
#
# PHẦN 2  — CHUẨN BỊ DỮ LIỆU
#   2.1  Train / Validation / Test Split
#   2.2  Feature Scaling
#   2.3  Encoding Categorical Variables
#   2.4  Xử lý Missing Data trong Pipeline
#   2.5  Imbalanced Data
#
# PHẦN 3  — SUPERVISED LEARNING: REGRESSION
#   3.1  Linear Regression
#   3.2  Ridge & Lasso (Regularization)
#   3.3  Polynomial Regression
#   3.4  Decision Tree Regressor
#   3.5  Random Forest Regressor ⭐
#   3.6  Gradient Boosting — XGBoost & LightGBM ⭐⭐
#   3.7  Regression Metrics
#
# PHẦN 4  — SUPERVISED LEARNING: CLASSIFICATION
#   4.1  Logistic Regression
#   4.2  K-Nearest Neighbors (KNN)
#   4.3  Support Vector Machine (SVM)
#   4.4  Decision Tree Classifier
#   4.5  Random Forest Classifier ⭐
#   4.6  Gradient Boosting Classifier ⭐⭐
#   4.7  Naive Bayes
#   4.8  Classification Metrics
#
# PHẦN 5  — MODEL EVALUATION & VALIDATION
#   5.1  Cross-Validation
#   5.2  Learning Curves
#   5.3  Confusion Matrix sâu hơn
#
# PHẦN 6  — HYPERPARAMETER TUNING
#   6.1  GridSearchCV
#   6.2  RandomizedSearchCV
#   6.3  Khi nào dùng cái nào
#
# PHẦN 7  — SKLEARN PIPELINES
#   7.1  Tại sao cần Pipeline?
#   7.2  ColumnTransformer
#   7.3  Full Pipeline thực tế
#
# PHẦN 8  — UNSUPERVISED LEARNING
#   8.1  K-Means Clustering
#   8.2  DBSCAN
#   8.3  PCA — Dimensionality Reduction
#   8.4  t-SNE — Visualization
#
# PHẦN 9  — PROJECT THỰC TẾ ĐẦU ĐẾN CUỐI
#   9.1  Bài toán: Dự đoán giá nhà
#   9.2  Full workflow hoàn chỉnh
#
# PHẦN 10 — LỘ TRÌNH HỌC TIẾP
# CHEAT SHEET


# ===========================================================================
# PHẦN 1: TỔNG QUAN MACHINE LEARNING
# ===========================================================================

# %% [markdown]
# ## 1.1 ML là gì? Tại sao quan trọng?
#
# LẬP TRÌNH TRUYỀN THỐNG:
#   Dữ liệu + Luật → Bạn viết → Kết quả
#   Ví dụ: if email có từ "trúng thưởng" → spam
#
# MACHINE LEARNING:
#   Dữ liệu + Kết quả → Máy tự học → Luật
#   Ví dụ: cho 10,000 email đã gán nhãn spam/not spam
#          → máy tự tìm ra đặc điểm của spam
#
# Tại sao ML quan trọng?
# Có những bài toán con người KHÔNG THỂ viết luật rõ ràng được:
#   - Nhận dạng giọng nói: không ai viết được hết luật âm thanh
#   - Dự đoán giá cổ phiếu: quá nhiều yếu tố
#   - Đề xuất sản phẩm Netflix/Spotify: 1 tỷ người × 10 triệu sản phẩm
#
# 💡 Định nghĩa (Arthur Samuel, 1959):
#    "Machine Learning là khả năng máy tính học từ kinh nghiệm
#     mà không cần lập trình tường minh."

# %% [markdown]
# ## 1.2 Ba Loại ML

# %%
# -----------------------------------------------------------------------------
# SUPERVISED LEARNING — Học có giám sát
# -----------------------------------------------------------------------------
# Dữ liệu huấn luyện CÓ nhãn (label)
# → Máy học ánh xạ từ Input → Output
#
# Ví dụ:
#   Ảnh     ——————→ Tên người (nhận dạng khuôn mặt)
#   Email   ————→ Spam / Not Spam
#   Thông số nhà → Giá nhà
#
# Hai dạng:
#   Regression     → Output là số liên tục (giá, nhiệt độ, điểm)
#   Classification → Output là nhãn rời rạc (spam/ham, cat/dog)

# -----------------------------------------------------------------------------
# UNSUPERVISED LEARNING — Học không có giám sát
# -----------------------------------------------------------------------------
# Dữ liệu KHÔNG có nhãn
# → Máy tự tìm pattern / cấu trúc ẩn
#
# Ví dụ:
#   Phân nhóm khách hàng tương tự nhau (clustering)
#   Nén ảnh, giảm chiều dữ liệu (dimensionality reduction)
#   Phát hiện giao dịch bất thường (anomaly detection)

# -----------------------------------------------------------------------------
# REINFORCEMENT LEARNING — Học tăng cường
# -----------------------------------------------------------------------------
# Agent tự khám phá môi trường, nhận reward/penalty
# → Học chiến lược tối ưu theo thời gian
# Ví dụ: AlphaGo, robot học đi, thuật toán trading
# (Không cover trong file này — cần nền tảng riêng)

print("1.2 - Ba loại ML: Supervised | Unsupervised | Reinforcement")

# %% [markdown]
# ## 1.3 End-to-End ML Workflow
#
# Đây là quy trình CHUẨN CÔNG NGHIỆP — mọi ML project đều đi qua đây:
#
# +-----------------------------------------------------------------+
# | BƯỚC 1 | Định nghĩa bài toán                                    |
# |        | → Regression hay Classification?                       |
# |        | → Metric nào để đo thành công?                         |
# +-----------------------------------------------------------------+
# | BƯỚC 2 | Thu thập & EDA dữ liệu                                 |
# |        | → Dữ liệu có đủ không? Phân phối thế nào?              |
# |        | → Missing values? Outliers? Imbalanced?                |
# +-----------------------------------------------------------------+
# | BƯỚC 3 | Chuẩn bị dữ liệu (Preprocessing)                      |
# |        | → Train/Test split → Scaling → Encoding                |
# +-----------------------------------------------------------------+
# | BƯỚC 4 | Chọn & huấn luyện mô hình                              |
# |        | → Bắt đầu đơn giản (Linear) → phức tạp (Ensemble)      |
# +-----------------------------------------------------------------+
# | BƯỚC 5 | Đánh giá mô hình                                       |
# |        | → Cross-validation → Metrics → Learning curves         |
# +-----------------------------------------------------------------+
# | BƯỚC 6 | Tinh chỉnh (Fine-tuning)                               |
# |        | → Hyperparameter tuning → Feature engineering          |
# +-----------------------------------------------------------------+
# | BƯỚC 7 | Đưa vào thực tế (Deploy)                               |
# |        | → Save model → API → Monitor                           |
# +-----------------------------------------------------------------+

# %% [markdown]
# ## 1.4 Overfitting, Underfitting & Bias-Variance Tradeoff
#
# Đây là khái niệm QUAN TRỌNG NHẤT trong ML.
# Hiểu rõ điều này = hiểu tại sao cần validation set, regularization,
# cross-validation.
#
# BIAS cao  = Underfitting
#   → Mô hình quá đơn giản, không học được pattern
#   → Train error cao, Test error cũng cao
#
# VARIANCE cao = Overfitting
#   → Mô hình quá phức tạp, học cả nhiễu (noise)
#   → Train error thấp, Test error rất cao
#
# MỤC TIÊU: Tìm điểm cân bằng giữa Bias và Variance

# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Tạo data thực: đường cong sin + nhiễu
np.random.seed(42)
x = np.sort(np.random.rand(30) * 10)
y = np.sin(x) + np.random.randn(30) * 0.3
x_plot = np.linspace(0, 10, 200)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for i, (degree, title, color) in enumerate(zip(
    [1, 3, 15],
    ["Underfitting (bậc 1)\nQuá đơn giản",
     "Vừa đẹp (bậc 3)\nKhái quát tốt",
     "Overfitting (bậc 15)\nHọc thuộc lòng"],
    ["#e74c3c", "#2ecc71", "#3498db"]
)):
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(x.reshape(-1, 1), y)
    y_pred = model.predict(x_plot.reshape(-1, 1))

    axes[i].scatter(x, y, color="gray", alpha=0.7, s=40, label="Data thực")
    axes[i].plot(x_plot, y_pred, color=color, linewidth=2.5)
    axes[i].set_title(title, fontsize=11, fontweight="bold")
    axes[i].set_ylim(-3, 3)

plt.suptitle("Underfitting vs Good Fit vs Overfitting", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()

# +----------------------------------------------------------+
# |              Bảng giải pháp Bias-Variance                |
# +----------------------+-----------------------------------+
# | Vấn đề               | Giải pháp                         |
# +----------------------+-----------------------------------+
# | Underfitting         | Mô hình phức tạp hơn, thêm        |
# |                      | features, giảm regularization     |
# +----------------------+-----------------------------------+
# | Overfitting          | Thêm data, regularization,        |
# |                      | dropout, cross-validation         |
# +----------------------+-----------------------------------+


# ===========================================================================
# PHẦN 2: CHUẨN BỊ DỮ LIỆU
# ===========================================================================

# %% [markdown]
# ## 2.1 Train / Validation / Test Split
#
# Vấn đề nếu train và test trên cùng 1 data:
# → Giống học sinh được xem đề trước khi thi
# → Điểm cao nhưng không phản ánh năng lực thật
#
# Cần 3 tập dữ liệu độc lập:
#
#   +--------------+--------------+--------------+
#   |  TRAIN (70%) |  VALID (15%) |  TEST  (15%) |
#   |  Dạy mô hình | Tune params  | Đánh giá lần |
#   |  học từ đây  | chọn mô hình | cuối (1 lần) |
#   +--------------+--------------+--------------+
#
# ⚠️ QUAN TRỌNG: Test set chỉ dùng 1 lần duy nhất ở cuối cùng!
#    Dùng nhiều lần = data leakage (gian lận vô tình)

# %%
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Tải dataset mẫu (California Housing)
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing(as_frame=True)
df = housing.frame

X = df.drop("MedHouseVal", axis=1)   # features
y = df["MedHouseVal"]                 # target (giá nhà)

# --- Cách 1: Chia đơn giản 80/20 ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,       # 20% cho test
    random_state=42      # đảm bảo kết quả reproducible
)
print(f"Train: {X_train.shape[0]} mẫu")   # 16512
print(f"Test:  {X_test.shape[0]} mẫu")    # 4128

# --- Cách 2: Chia 3 tập train/val/test ---
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.176, random_state=42)
# 0.176 ≈ 0.15 / 0.85 để test và val đều ~15%
print(f"Train: {X_train.shape[0]} | Val: {X_val.shape[0]} | Test: {X_test.shape[0]}")

# --- Stratified split: quan trọng cho Classification ---
# Đảm bảo tỉ lệ nhãn giống nhau ở train và test
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer(as_frame=True)
X_c = data.data
y_c = data.target   # 0 = malignant (ác tính), 1 = benign (lành tính)

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X_c, y_c,
    test_size=0.2,
    stratify=y_c,    # ← ĐẢM BẢO tỉ lệ 0/1 giống nhau ở cả 2 tập
    random_state=42
)
print(f"\nTỉ lệ malignant trong train: {y_train_c.mean():.3f}")
print(f"Tỉ lệ malignant trong test:  {y_test_c.mean():.3f}")
# Hai giá trị phải gần bằng nhau → stratify thành công

# 💡 Tóm tắt 1 dòng:
# Luôn stratify=y cho classification, random_state=42 cho reproducible.

# %% [markdown]
# ## 2.2 Feature Scaling — Chuẩn Hóa Đặc Trưng
#
# Tại sao phải scale?
#   Diện tích: 30 → 200 m²
#   Số phòng:   1 → 5
#
#   KNN/SVM/Gradient Descent tính khoảng cách:
#   distance = sqrt((200-30)² + (5-1)²) ≈ 170
#   → Feature "Diện tích" THỐNG TRỊ hoàn toàn vì đơn vị lớn hơn
#   → Số phòng gần như bị bỏ qua!
#
#   Sau khi scale về cùng khoảng → cả hai ảnh hưởng ngang nhau

# %%
from sklearn.preprocessing import StandardScaler, MinMaxScaler

luong = np.array([[15], [20], [18], [12], [25], [30]])

# --- StandardScaler: Z-score normalization ---
# Công thức: z = (x - mean) / std
# Kết quả: mean=0, std=1
scaler_std = StandardScaler()
luong_std = scaler_std.fit_transform(luong)
print("StandardScaler:")
print(luong_std.T)
print(f"Mean: {luong_std.mean():.2f}, Std: {luong_std.std():.2f}")

# --- MinMaxScaler: rescale về khoảng [0, 1] ---
# Công thức: x_scaled = (x - min) / (max - min)
# Dùng khi: muốn giữ nguyên phân phối, không có outliers
scaler_mm = MinMaxScaler()
luong_mm = scaler_mm.fit_transform(luong)
print("\nMinMaxScaler:")
print(luong_mm.T)
print(f"Min: {luong_mm.min():.2f}, Max: {luong_mm.max():.2f}")

# --- ⚠️ QUY TẮC VÀNG: fit CHỈ trên train, transform cả train lẫn test ---
# SAI (data leakage):
#   scaler.fit_transform(X)   # fit toàn bộ → biết thông tin test set!
#
# ĐÚNG:
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # học mean/std từ TRAIN
X_test_scaled  = scaler.transform(X_test)        # dùng CÙNG mean/std để transform test

# +------------------+----------------------+----------------------+
# | Khi nào dùng     | StandardScaler       | MinMaxScaler         |
# +------------------+----------------------+----------------------+
# | Có outliers      | ✅ Tốt hơn           | ❌ Outlier kéo lệch  |
# | Neural Networks  | ✅ Hay dùng          | ✅ Hay dùng          |
# | KNN, SVM         | ✅ Tốt               | ✅ Được              |
# | Cần về [0,1]     | ❌                   | ✅                   |
# +------------------+----------------------+----------------------+

# %% [markdown]
# ## 2.3 Encoding Categorical Variables
#
# ML models chỉ hiểu SỐ, không hiểu chữ.
# "Hà Nội", "TP.HCM", "Đà Nẵng" phải chuyển thành số.
#
# Ordinal Encoding → khi category CÓ THỨ TỰ: Junior < Mid < Senior
# One-Hot Encoding → khi category KHÔNG có thứ tự: IT, KD, HR

# %%
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

df_enc = pd.DataFrame({
    "Cap_bac": ["Junior", "Senior", "Mid", "Junior", "Senior"],  # có thứ tự
    "Phong":   ["IT", "KD", "IT", "HR", "KD"],                  # không có thứ tự
    "Luong":   [15, 25, 18, 14, 24]
})

# --- Ordinal Encoding: khi category CÓ THỨ TỰ ---
oe = OrdinalEncoder(categories=[["Junior", "Mid", "Senior"]])
df_enc["Cap_bac_encoded"] = oe.fit_transform(df_enc[["Cap_bac"]])
# Junior→0, Mid→1, Senior→2 ✅
print("Ordinal Encoding (Cap_bac):")
print(df_enc[["Cap_bac", "Cap_bac_encoded"]])

# --- One-Hot Encoding: khi category KHÔNG có thứ tự ---
# ❌ KHÔNG dùng Ordinal cho Phong vì IT=0, KD=1 ngụ ý KD > IT (sai!)
ohe = OneHotEncoder(sparse_output=False, drop="first")
# drop="first": xóa 1 cột tránh multicollinearity (dummy variable trap)
phong_encoded = ohe.fit_transform(df_enc[["Phong"]])
print("\nOne-Hot Encoding (Phong):")
print(phong_encoded)

# --- Pandas get_dummies (cách nhanh) ---
df_dummies = pd.get_dummies(df_enc, columns=["Phong"], drop_first=True)
print("\nDataFrame sau get_dummies:")
print(df_dummies)

# --- Label Encoding — Chỉ cho Target (y), KHÔNG dùng cho features ---
from sklearn.preprocessing import LabelEncoder
y_labels = ["spam", "ham", "ham", "spam", "spam"]
le = LabelEncoder()
y_encoded = le.fit_transform(y_labels)   # ham=0, spam=1
print(f"\nLabel Encoding: {y_encoded}")  # [1 0 0 1 1]

# %% [markdown]
# ## 2.4 Xử Lý Missing Data trong ML Pipeline

# %%
from sklearn.impute import SimpleImputer

# Data có NaN
X_missing = np.array([[1, 2, np.nan],
                       [4, np.nan, 6],
                       [7, 8, 9]])

# --- Imputation: điền giá trị vào chỗ thiếu ---
# strategy: "mean", "median", "most_frequent", "constant"
imp_mean   = SimpleImputer(strategy="mean")
imp_median = SimpleImputer(strategy="median")

print("Mean imputation:\n",   imp_mean.fit_transform(X_missing))
print("Median imputation:\n", imp_median.fit_transform(X_missing))

# Khi nào dùng gì:
# mean          → khi data phân phối chuẩn, không outliers
# median        → khi có outliers (an toàn hơn)
# most_frequent → cho categorical
# constant      → khi biết giá trị mặc định

# %% [markdown]
# ## 2.5 Imbalanced Data — Dữ Liệu Mất Cân Bằng
#
# Ví dụ: phát hiện gian lận (fraud detection)
# 99% giao dịch bình thường, 1% gian lận
# Nếu model dự đoán TẤT CẢ là "bình thường":
# → Accuracy = 99% nhưng VÔ DỤNG!

# %%
from sklearn.utils.class_weight import compute_class_weight

# --- Cách 1: Class weights ---
# Nói với model "trường hợp hiếm quan trọng hơn"
y_train_imb = np.array([0]*990 + [1]*10)  # 99% class 0, 1% class 1

weights = compute_class_weight(
    class_weight="balanced",
    classes=np.unique(y_train_imb),
    y=y_train_imb
)
class_weight_dict = dict(zip(np.unique(y_train_imb), weights))
print(class_weight_dict)   # {0: 0.505, 1: 50.5} → class 1 được nhân 100x

# Truyền vào model:
from sklearn.ensemble import RandomForestClassifier
model_balanced = RandomForestClassifier(class_weight="balanced", random_state=42)

# --- Cách 2: SMOTE — tạo thêm mẫu cho class thiểu số ---
# pip install imbalanced-learn
# (Chỉ dùng trên TRAIN set, KHÔNG dùng trên test!)
try:
    from imblearn.over_sampling import SMOTE
    X_imb = np.random.rand(1000, 5)
    y_imb = np.array([0]*990 + [1]*10)

    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_imb, y_imb)
    print(f"Trước SMOTE: {np.bincount(y_imb)}")        # [990  10]
    print(f"Sau  SMOTE:  {np.bincount(y_resampled)}")  # [990 990]
except ImportError:
    print("Cài imbalanced-learn: pip install imbalanced-learn")


# ===========================================================================
# PHẦN 3: SUPERVISED LEARNING — REGRESSION
# ===========================================================================

# %% [markdown]
# ## 3.1 Linear Regression
#
# Tìm đường thẳng (hoặc mặt phẳng) khớp nhất với dữ liệu.
#
#   y = w0 + w1x₁ + w₂x₂ + ... + wnxₙ + ε
#
#   w0       = intercept (bias)
#   w1...wn  = coefficients (trọng số mỗi feature)
#   ε        = sai số
#
# Mục tiêu: Tìm w sao cho tổng (y_pred - y_true)² nhỏ nhất
#            → Gọi là "Ordinary Least Squares" (OLS)

# %%
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dữ liệu California Housing
housing = fetch_california_housing(as_frame=True)
X = housing.data
y = housing.target   # giá nhà trung bình (×$100,000)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Huấn luyện
lr = LinearRegression()
lr.fit(X_train, y_train)

# Dự đoán & Đánh giá
y_pred = lr.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2   = r2_score(y_test, y_pred)
print(f"RMSE: {rmse:.4f}")   # sai số trung bình
print(f"R²:   {r2:.4f}")     # 1.0 = hoàn hảo, 0 = model vô dụng

# Xem coefficients
coef_df = pd.DataFrame({
    "Feature":     X.columns,
    "Coefficient": lr.coef_
}).sort_values("Coefficient", key=abs, ascending=False)
print("\nCác hệ số quan trọng nhất:")
print(coef_df.head())
print(f"\nIntercept (w0): {lr.intercept_:.4f}")

# Visualize: Predicted vs Actual
plt.figure(figsize=(7, 5))
plt.scatter(y_test, y_pred, alpha=0.3, s=20, color="steelblue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
         "r--", linewidth=2, label="Đường lý tưởng")
plt.xlabel("Giá thực")
plt.ylabel("Giá dự đoán")
plt.title(f"Linear Regression — R² = {r2:.3f}")
plt.legend()
plt.tight_layout()
plt.show()

# 💡 Khi nào dùng Linear Regression:
# - Mối quan hệ giữa X và y gần tuyến tính
# - Cần giải thích model (interpretability cao)
# - Baseline nhanh trước khi thử mô hình phức tạp hơn

# %% [markdown]
# ## 3.2 Ridge & Lasso — Regularization
#
# Vấn đề: Khi có quá nhiều features hoặc features tương quan cao
# → Coefficients có thể rất lớn → model overfit
#
# Giải pháp: Regularization = phạt model khi coefficients quá lớn
#
# Ridge (L2): Loss = OLS_Loss + α × Σ(wᵢ²)
#   → Giảm TẤT CẢ coefficients về gần 0, không về đúng 0
#
# Lasso (L1): Loss = OLS_Loss + α × Σ|wᵢ|
#   → Đưa một số coefficients về ĐÚNG 0 → tự động chọn features
#
# α (alpha) = hyperparameter điều chỉnh mức độ phạt
#   α = 0 → giống Linear Regression thường
#   α lớn → coefficients nhỏ hơn, model đơn giản hơn

# %%
from sklearn.linear_model import Ridge, Lasso, RidgeCV, LassoCV
from sklearn.pipeline import Pipeline

# --- Ridge Regression ---
ridge = Pipeline([
    ("scaler", StandardScaler()),   # bắt buộc scale trước regularization
    ("model",  Ridge(alpha=1.0))
])
ridge.fit(X_train, y_train)
print(f"Ridge R²: {ridge.score(X_test, y_test):.4f}")

# --- Lasso Regression ---
lasso = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  Lasso(alpha=0.01))
])
lasso.fit(X_train, y_train)
print(f"Lasso R²: {lasso.score(X_test, y_test):.4f}")

# Xem features bị Lasso loại bỏ (coefficient = 0)
lasso_coef = lasso.named_steps["model"].coef_
zero_features = X.columns[lasso_coef == 0].tolist()
print(f"Features bị Lasso loại: {zero_features}")

# --- Tự động chọn alpha tốt nhất bằng Cross-Validation ---
alphas = [0.001, 0.01, 0.1, 1, 10, 100]
ridge_cv = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  RidgeCV(alphas=alphas, cv=5))
])
ridge_cv.fit(X_train, y_train)
print(f"\nRidge alpha tối ưu: {ridge_cv.named_steps['model'].alpha_}")
print(f"RidgeCV R²: {ridge_cv.score(X_test, y_test):.4f}")

# +------------+---------------+--------------------------+
# |            | Ridge         | Lasso                    |
# +------------+---------------+--------------------------+
# | Công thức  | Σwᵢ²          | Σ|wᵢ|                   |
# | Tác dụng   | Shrink tất cả | Xóa bớt features         |
# | Dùng khi   | Nhiều features| Muốn feature selection   |
# | Kết quả    | Không sparse  | Sparse (nhiều coef=0)    |
# +------------+---------------+--------------------------+

# %% [markdown]
# ## 3.3 Polynomial Regression

# %%
from sklearn.preprocessing import PolynomialFeatures

# Dữ liệu có quan hệ phi tuyến
np.random.seed(42)
x_poly = np.sort(np.random.rand(60) * 6 - 3)   # từ -3 đến 3
y_poly = x_poly**3 - 2*x_poly + np.random.randn(60) * 1.5

x_poly_plot = np.linspace(-3, 3, 200).reshape(-1, 1)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
for ax, degree in zip(axes, [1, 3, 7]):
    model = Pipeline([
        ("poly",   PolynomialFeatures(degree=degree, include_bias=False)),
        ("linear", LinearRegression())
    ])
    model.fit(x_poly.reshape(-1, 1), y_poly)
    y_plot = model.predict(x_poly_plot)
    score = model.score(x_poly.reshape(-1, 1), y_poly)

    ax.scatter(x_poly, y_poly, alpha=0.6, s=30, color="gray")
    ax.plot(x_poly_plot, y_plot, color="red", linewidth=2)
    ax.set_title(f"Bậc {degree} — R²={score:.3f}")
    ax.set_ylim(-12, 12)

plt.suptitle("Polynomial Regression — Tăng độ phức tạp", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.show()
# Bậc 1: underfitting | Bậc 3: tốt nhất | Bậc 7: bắt đầu overfit

# %% [markdown]
# ## 3.4 Decision Tree Regressor
#
# Decision Tree chia dữ liệu thành các vùng nhỏ:
#
#   Diện tích > 80m²?
#   +-- Có → Số phòng > 3?
#   |         +-- Có → Giá = 5 tỷ
#   |         +-- Không → Giá = 3.5 tỷ
#   +-- Không → Quận nội thành?
#               +-- Có → Giá = 2.5 tỷ
#               +-- Không → Giá = 1.5 tỷ
#
# Mỗi nút = 1 câu hỏi về feature
# Mỗi lá  = 1 dự đoán (trung bình của nhóm)

# %%
from sklearn.tree import DecisionTreeRegressor, plot_tree

dt = DecisionTreeRegressor(
    max_depth=4,         # chiều sâu tối đa của cây
    min_samples_leaf=20, # mỗi lá cần ít nhất 20 mẫu
    random_state=42
)
dt.fit(X_train, y_train)

print(f"Train R²: {dt.score(X_train, y_train):.4f}")
print(f"Test  R²: {dt.score(X_test,  y_test):.4f}")

# Xem cây
plt.figure(figsize=(20, 8))
plot_tree(dt, feature_names=X.columns,
          filled=True, rounded=True,
          fontsize=8, max_depth=3)   # chỉ hiển thị 3 tầng đầu
plt.title("Decision Tree Structure")
plt.tight_layout()
plt.show()

# Feature importance
fi = pd.Series(dt.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nFeature Importance:")
print(fi.round(4))

# ⚠️ VẤN ĐỀ CỦA DECISION TREE ĐƠN LẺ:
# max_depth nhỏ → underfitting
# max_depth lớn → overfitting (học thuộc từng điểm)
# Giải pháp → Random Forest (Phần 3.5)

# %% [markdown]
# ## 3.5 Random Forest Regressor ⭐
#
# Random Forest là một trong những thuật toán MẠNH VÀ ỔN ĐỊNH NHẤT.
#
# Ý tưởng: "Wisdom of the Crowd" (Trí tuệ đám đông)
#
#   1 cây quyết định → dễ overfit, không ổn định
#
#   Random Forest = 100+ cây KHÁC NHAU
#   → Mỗi cây học từ 1 tập dữ liệu ngẫu nhiên (bootstrap)
#   → Mỗi cây chỉ dùng ngẫu nhiên một số features ở mỗi nút
#   → Kết quả cuối = TRUNG BÌNH của 100+ dự đoán
#
#   Tại sao hiệu quả?
#   Mỗi cây mắc sai lầm ở các chỗ KHÁC NHAU
#   → Trung bình nhiều cây → sai lầm triệt tiêu nhau
#   → Kết quả ổn định, ít overfit
#   → Kỹ thuật này gọi là BAGGING (Bootstrap AGGregation)

# %%
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(
    n_estimators=100,    # 100 cây — thường đủ
    max_depth=None,      # mỗi cây phát triển hết
    min_samples_leaf=5,  # mỗi lá cần ít nhất 5 mẫu
    max_features="sqrt", # mỗi nút chỉ dùng √n features → tăng đa dạng
    n_jobs=-1,           # dùng tất cả CPU cores → nhanh hơn
    random_state=42
)
rf.fit(X_train, y_train)

print(f"Train R²: {rf.score(X_train, y_train):.4f}")   # thường rất cao
print(f"Test  R²: {rf.score(X_test,  y_test):.4f}")    # mới là thước đo thật

# Feature importance
fi_rf = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)

plt.figure(figsize=(8, 5))
fi_rf.plot(kind="barh", color="steelblue")
plt.xlabel("Importance")
plt.title("Random Forest — Feature Importance")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 3.6 Gradient Boosting — XGBoost & LightGBM ⭐⭐
#
# Thuật toán MẠNH NHẤT cho dữ liệu dạng bảng (tabular data)
# — thống trị Kaggle.
#
# Ý tưởng: Học từ sai lầm
#
#   Random Forest:    nhiều cây SONG SONG → trung bình
#   Gradient Boosting: nhiều cây NỐI TIẾP → mỗi cây sửa lỗi cây trước
#
#   Bước 1: Cây 1 dự đoán → sai số = [+2, -1, +3, ...]
#   Bước 2: Cây 2 học sửa SAI SỐ của cây 1
#   Bước 3: Cây 3 học sửa SAI SỐ còn lại
#   ...
#   Bước 100: Dự đoán cuối = tổng tất cả cây × learning_rate
#
#   learning_rate nhỏ + nhiều cây → chính xác hơn nhưng chậm hơn

# %%
# Cài đặt: pip install xgboost lightgbm
try:
    import xgboost as xgb
    from sklearn.metrics import r2_score as r2

    # --- XGBoost ---
    xgb_model = xgb.XGBRegressor(
        n_estimators=500,
        learning_rate=0.05,     # mỗi cây đóng góp 5%
        max_depth=5,
        subsample=0.8,          # mỗi cây dùng 80% data → giảm overfit
        colsample_bytree=0.8,   # mỗi cây dùng 80% features
        early_stopping_rounds=50,
        eval_metric="rmse",
        random_state=42,
        n_jobs=-1,
        verbosity=0
    )
    xgb_model.fit(
        X_train, y_train,
        eval_set=[(X_test, y_test)],
        verbose=False
    )
    y_pred_xgb = xgb_model.predict(X_test)
    print(f"XGBoost R²:   {r2(y_test, y_pred_xgb):.4f}")
    print(f"XGBoost RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_xgb)):.4f}")
except ImportError:
    print("Cài XGBoost: pip install xgboost")

try:
    import lightgbm as lgb

    # --- LightGBM (nhanh hơn XGBoost ~10x với data lớn) ---
    lgb_model = lgb.LGBMRegressor(
        n_estimators=500,
        learning_rate=0.05,
        max_depth=5,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1,
        verbose=-1
    )
    lgb_model.fit(
        X_train, y_train,
        eval_set=[(X_test, y_test)],
        callbacks=[lgb.early_stopping(50, verbose=False),
                   lgb.log_evaluation(0)]
    )
    y_pred_lgb = lgb_model.predict(X_test)
    print(f"\nLightGBM R²:   {r2(y_test, y_pred_lgb):.4f}")
    print(f"LightGBM RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_lgb)):.4f}")
except ImportError:
    print("Cài LightGBM: pip install lightgbm")

# +------------------+----------+----------+---------------+
# |                  | XGBoost  | LightGBM | Random Forest |
# +------------------+----------+----------+---------------+
# | Tốc độ           | Nhanh    | Rất nhanh| Vừa           |
# | Accuracy         | Rất cao  | Rất cao  | Cao           |
# | Data nhỏ (<10K)  | ✅       | ✅       | ✅            |
# | Data lớn (>1M)   | Chậm     | ✅       | ✅            |
# | Cần tuning       | Nhiều    | Vừa      | Ít            |
# +------------------+----------+----------+---------------+

# %% [markdown]
# ## 3.7 Regression Metrics — Đo Hiệu Quả

# %%
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

y_true_ex = np.array([3.0, 2.5, 4.0, 5.0, 3.5])
y_pred_ex = np.array([2.8, 2.6, 3.8, 5.2, 3.3])

# MAE: Trung bình |sai số| — ít nhạy với outliers
mae = mean_absolute_error(y_true_ex, y_pred_ex)
print(f"MAE:  {mae:.4f}")   # dễ giải thích, cùng đơn vị với y

# MSE: Trung bình (sai số)² — phạt sai số lớn MẠNH hơn
mse = mean_squared_error(y_true_ex, y_pred_ex)
print(f"MSE:  {mse:.4f}")

# RMSE: Căn bậc 2 của MSE — về lại đơn vị gốc
rmse = np.sqrt(mse)
print(f"RMSE: {rmse:.4f}")

# R²: Tỉ lệ variance được giải thích bởi model
# R²=1: hoàn hảo | R²=0: bằng dự đoán trung bình | R²<0: tệ hơn
r2 = r2_score(y_true_ex, y_pred_ex)
print(f"R²:   {r2:.4f}")

# Khi nào dùng:
# MAE  → khi outliers không đáng lo, muốn giải thích đơn giản
# RMSE → khi sai số lớn rất đáng lo (phạt nặng sai lầm lớn)
# R²   → để so sánh models với nhau (cùng dataset)


# ===========================================================================
# PHẦN 4: SUPERVISED LEARNING — CLASSIFICATION
# ===========================================================================

# Setup dữ liệu chung cho Phần 4
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

data_bc = load_breast_cancer(as_frame=True)
X_clf = data_bc.data
y_clf = data_bc.target   # 0=malignant (ác tính), 1=benign (lành tính)

X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X_clf, y_clf, test_size=0.2, stratify=y_clf, random_state=42
)
scaler_clf = StandardScaler()
X_train_s = scaler_clf.fit_transform(X_train_clf)
X_test_s  = scaler_clf.transform(X_test_clf)

# %% [markdown]
# ## 4.1 Logistic Regression
#
# Tại sao không dùng Linear Regression cho Classification?
#   Linear Regression có thể cho kết quả 1.5, -0.3, 2.7 → vô nghĩa!
#
# Logistic Regression dùng hàm Sigmoid:
#   σ(z) = 1 / (1 + e^(-z))
#   → Kết quả luôn trong (0, 1) = xác suất
#   → P(spam) = 0.87 → "87% khả năng là spam"
#   → Ngưỡng 0.5: P ≥ 0.5 → Spam, P < 0.5 → Not Spam

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

lr_clf = LogisticRegression(
    C=1.0,            # C = 1/alpha → C nhỏ = regularization mạnh hơn
    max_iter=1000,    # tăng nếu bị warning "did not converge"
    random_state=42
)
lr_clf.fit(X_train_s, y_train_clf)

y_pred_lr       = lr_clf.predict(X_test_s)          # class dự đoán (0 hoặc 1)
y_pred_lr_proba = lr_clf.predict_proba(X_test_s)    # xác suất mỗi class

print("Xác suất 5 mẫu đầu tiên:")
print(y_pred_lr_proba[:5].round(3))
# Cột 0 = P(malignant), Cột 1 = P(benign)

print("\nClassification Report:")
print(classification_report(y_test_clf, y_pred_lr, target_names=data_bc.target_names))

# Confusion Matrix
cm = confusion_matrix(y_test_clf, y_pred_lr)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=data_bc.target_names,
            yticklabels=data_bc.target_names)
plt.title("Confusion Matrix — Logistic Regression")
plt.ylabel("Thực tế")
plt.xlabel("Dự đoán")
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 4.2 K-Nearest Neighbors (KNN)
#
# "Nói cho tôi biết bạn bè của bạn, tôi sẽ biết bạn là ai."
#
# Để phân loại điểm mới X:
#   1. Tính khoảng cách từ X đến TẤT CẢ điểm training
#   2. Lấy K điểm gần nhất
#   3. Nhãn nào xuất hiện nhiều nhất trong K điểm = kết quả
#
# ⚠️ Điểm yếu:
#   - Chậm khi predict (tính khoảng cách với TOÀN BỘ training data)
#   - Không tốt với nhiều features (curse of dimensionality)
#   - Nhạy cảm với scale → PHẢI StandardScaler trước

# %%
from sklearn.neighbors import KNeighborsClassifier

# Ảnh hưởng của K đến accuracy
k_values = range(1, 31)
train_scores_knn, test_scores_knn = [], []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_s, y_train_clf)
    train_scores_knn.append(knn.score(X_train_s, y_train_clf))
    test_scores_knn.append(knn.score(X_test_s, y_test_clf))

plt.figure(figsize=(9, 4))
plt.plot(k_values, train_scores_knn, "b-o", ms=4, label="Train Accuracy")
plt.plot(k_values, test_scores_knn,  "r-o", ms=4, label="Test Accuracy")
plt.xlabel("Giá trị K")
plt.ylabel("Accuracy")
plt.title("KNN: K nhỏ=overfit, K lớn=underfit")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# K tốt nhất
optimal_k = list(k_values)[np.argmax(test_scores_knn)]
print(f"K tốt nhất: {optimal_k}")

knn_best = KNeighborsClassifier(n_neighbors=optimal_k)
knn_best.fit(X_train_s, y_train_clf)
print(f"Accuracy: {knn_best.score(X_test_s, y_test_clf):.4f}")

# %% [markdown]
# ## 4.3 Support Vector Machine (SVM)
#
# Tìm "đường ranh giới" phân chia 2 lớp với khoảng cách LỚN NHẤT:
#
#   Support Vectors = các điểm nằm GẦN NHẤT với đường ranh giới
#   Margin = khoảng cách từ đường đến support vectors
#
#   Với dữ liệu không tách được tuyến tính → dùng Kernel Trick:
#   → Đưa data lên chiều không gian cao hơn nơi có thể tách tuyến tính
#
# Kernel phổ biến:
#   "linear" → tách tuyến tính (nhanh)
#   "rbf"    → Gaussian kernel (phổ biến nhất ✅)
#   "poly"   → Polynomial kernel
#
# ⚠️ Điểm yếu: Chậm với data lớn (>100K mẫu)

# %%
from sklearn.svm import SVC

# SVM LUÔN CẦN SCALE
svm = SVC(
    C=1.0,                  # điều chỉnh margin (C lớn = ít bỏ qua outliers)
    kernel="rbf",           # Radial Basis Function — phổ biến nhất
    gamma="scale",          # tự động scale gamma
    probability=True,       # cho phép predict_proba
    random_state=42
)
svm.fit(X_train_s, y_train_clf)
print(f"SVM Accuracy: {svm.score(X_test_s, y_test_clf):.4f}")

# %% [markdown]
# ## 4.4–4.5 Decision Tree & Random Forest Classifier

# %%
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Decision Tree Classifier
dt_clf = DecisionTreeClassifier(
    max_depth=5,
    min_samples_leaf=10,
    criterion="gini",    # "gini" hoặc "entropy" — thường không khác nhiều
    random_state=42
)
dt_clf.fit(X_train_clf, y_train_clf)  # không cần scale cho tree-based models
print(f"DT Train: {dt_clf.score(X_train_clf, y_train_clf):.4f}")
print(f"DT Test:  {dt_clf.score(X_test_clf,  y_test_clf):.4f}")

# Random Forest Classifier ⭐
rf_clf = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    min_samples_leaf=5,
    max_features="sqrt",
    class_weight="balanced",  # quan trọng nếu data mất cân bằng
    n_jobs=-1,
    random_state=42
)
rf_clf.fit(X_train_clf, y_train_clf)
print(f"\nRF Train: {rf_clf.score(X_train_clf, y_train_clf):.4f}")
print(f"RF Test:  {rf_clf.score(X_test_clf,  y_test_clf):.4f}")

y_proba_rf = rf_clf.predict_proba(X_test_clf)
print(f"\nP(class 0) | P(class 1) cho 3 mẫu đầu:")
print(y_proba_rf[:3].round(3))

# %% [markdown]
# ## 4.6 Gradient Boosting Classifier ⭐⭐

# %%
try:
    import xgboost as xgb
    from sklearn.metrics import classification_report

    xgb_clf = xgb.XGBClassifier(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=4,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss",
        early_stopping_rounds=30,
        random_state=42,
        n_jobs=-1,
        verbosity=0
    )
    xgb_clf.fit(
        X_train_clf, y_train_clf,
        eval_set=[(X_test_clf, y_test_clf)],
        verbose=False
    )
    y_pred_xgb_clf = xgb_clf.predict(X_test_clf)
    print("XGBoost Classification Report:")
    print(classification_report(y_test_clf, y_pred_xgb_clf,
                                 target_names=data_bc.target_names))
except ImportError:
    print("Cài XGBoost: pip install xgboost")

# %% [markdown]
# ## 4.7 Naive Bayes

# %%
from sklearn.naive_bayes import GaussianNB, MultinomialNB

# GaussianNB: khi features là số liên tục
gnb = GaussianNB()
gnb.fit(X_train_s, y_train_clf)
print(f"Gaussian NB Accuracy: {gnb.score(X_test_s, y_test_clf):.4f}")

# MultinomialNB: khi features là tần số (text classification)
from sklearn.feature_extraction.text import CountVectorizer

emails = ["buy now free money", "meeting tomorrow 10am", "win prize free"]
labels = [1, 0, 1]   # 1=spam, 0=not spam
vec = CountVectorizer()
X_email = vec.fit_transform(emails)
mnb = MultinomialNB()
mnb.fit(X_email, labels)

new_email = vec.transform(["free prize money"])
print(f"Spam probability: {mnb.predict_proba(new_email)[0][1]:.4f}")

# Ưu điểm NB: cực nhanh, tốt với text, ít data cũng học được
# Nhược điểm: giả định features độc lập nhau (thường không đúng thực tế)

# %% [markdown]
# ## 4.8 Classification Metrics — Đo Hiệu Quả Phân Loại
#
# Accuracy không phải lúc nào cũng đủ!
#
# Ví dụ: phát hiện bệnh hiếm (1% dân số có bệnh)
# Model luôn nói "không có bệnh" → Accuracy=99% nhưng VÔ DỤNG!
#
# +--------------------------------------------------------------+
# |               CONFUSION MATRIX — Bảng chân lý               |
# |                                                              |
# |                  Dự đoán: Negative  |  Positive             |
# | Thực tế: Negative       [   TN      |    FP   ]             |
# | Thực tế: Positive       [   FN      |    TP   ]             |
# |                                                              |
# | TN = True Negative  (nói không bệnh, thật không bệnh)  ✅   |
# | TP = True Positive  (nói có bệnh, thật có bệnh)         ✅   |
# | FP = False Positive (nói có bệnh, thật không bệnh)      ❌   |  Type I Error
# | FN = False Negative (nói không bệnh, thật có bệnh)      ❌   |  Type II Error
# +--------------------------------------------------------------+
#
# Accuracy  = (TP+TN)/Total   → dùng khi classes cân bằng
# Precision = TP/(TP+FP)      → quan trọng khi FP nguy hiểm (spam filter)
# Recall    = TP/(TP+FN)      → quan trọng khi FN nguy hiểm (phát hiện ung thư)
# F1-score  = 2×(P×R)/(P+R)  → cân bằng cả hai, dùng khi classes mất cân bằng

# %%
from sklearn.metrics import (accuracy_score, precision_score,
                              recall_score, f1_score,
                              roc_auc_score, roc_curve)

y_true_ex2 = np.array([0, 1, 1, 0, 1, 1, 0, 0, 1, 0])
y_pred_ex2 = np.array([0, 1, 0, 0, 1, 1, 0, 1, 1, 0])

print(f"Accuracy:  {accuracy_score(y_true_ex2, y_pred_ex2):.4f}")
print(f"Precision: {precision_score(y_true_ex2, y_pred_ex2):.4f}")
print(f"Recall:    {recall_score(y_true_ex2, y_pred_ex2):.4f}")
print(f"F1-score:  {f1_score(y_true_ex2, y_pred_ex2):.4f}")

# --- ROC-AUC CURVE ---
# Thay đổi ngưỡng quyết định (0.5 → 0.3, 0.7, ...)
# AUC = Area Under Curve → 1.0 = hoàn hảo, 0.5 = random
y_proba_test = rf_clf.predict_proba(X_test_clf)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test_clf, y_proba_test)
auc = roc_auc_score(y_test_clf, y_proba_test)

plt.figure(figsize=(7, 5))
plt.plot(fpr, tpr, color="steelblue", linewidth=2,
         label=f"ROC Curve (AUC = {auc:.4f})")
plt.plot([0,1],[0,1], "k--", linewidth=1, label="Random (AUC=0.5)")
plt.fill_between(fpr, tpr, alpha=0.1, color="steelblue")
plt.xlabel("False Positive Rate (1 - Specificity)")
plt.ylabel("True Positive Rate (Recall)")
plt.title("ROC Curve")
plt.legend()
plt.tight_layout()
plt.show()

# --- Chọn ngưỡng tối ưu ---
# Mặc định threshold = 0.5, nhưng có thể không phải tốt nhất!
f1_scores_thresh = []
for t in thresholds:
    y_pred_t = (y_proba_test >= t).astype(int)
    f1_scores_thresh.append(f1_score(y_test_clf, y_pred_t))

best_threshold = thresholds[np.argmax(f1_scores_thresh)]
print(f"\nThreshold tối ưu cho F1: {best_threshold:.4f}")
y_pred_optimal = (y_proba_test >= best_threshold).astype(int)
print(f"F1 với threshold {best_threshold:.2f}: {f1_score(y_test_clf, y_pred_optimal):.4f}")


# ===========================================================================
# PHẦN 5: MODEL EVALUATION & VALIDATION
# ===========================================================================

# %% [markdown]
# ## 5.1 Cross-Validation — Đánh Giá Đáng Tin Cậy Hơn
#
# Vấn đề với train/test split đơn giản:
#   Lần 1: random_state=42 → Test R²=0.82
#   Lần 2: random_state=7  → Test R²=0.79
#   → Kết quả dao động, không đáng tin!
#
# Giải pháp: K-Fold Cross-Validation
#
#   Chia data thành K phần (fold) bằng nhau:
#   Fold 1: [TEST][TRAIN][TRAIN][TRAIN][TRAIN]
#   Fold 2: [TRAIN][TEST][TRAIN][TRAIN][TRAIN]
#   Fold 3: [TRAIN][TRAIN][TEST][TRAIN][TRAIN]
#   ...
#   → Train K lần, lấy TRUNG BÌNH K kết quả
#   → Đánh giá đáng tin cậy hơn nhiều

# %%
from sklearn.model_selection import cross_val_score, StratifiedKFold, cross_validate

# K-Fold cho Regression
from sklearn.linear_model import Ridge

cv_scores = cross_val_score(
    Ridge(alpha=1.0),
    X, y,
    cv=5,                              # 5-fold
    scoring="neg_mean_squared_error"   # sklearn dùng âm (cao hơn = tốt hơn)
)
rmse_scores = np.sqrt(-cv_scores)
print(f"RMSE mỗi fold: {rmse_scores.round(4)}")
print(f"RMSE trung bình: {rmse_scores.mean():.4f} ± {rmse_scores.std():.4f}")

# Stratified K-Fold cho Classification (giữ tỉ lệ class)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_clf_scores = cross_val_score(
    RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
    X_clf, y_clf,
    cv=skf,
    scoring="roc_auc"
)
print(f"\nROC-AUC mỗi fold: {cv_clf_scores.round(4)}")
print(f"ROC-AUC trung bình: {cv_clf_scores.mean():.4f} ± {cv_clf_scores.std():.4f}")

# cross_validate: lấy nhiều metrics cùng lúc
results_cv = cross_validate(
    RandomForestClassifier(n_estimators=100, random_state=42),
    X_clf, y_clf,
    cv=5,
    scoring=["accuracy", "roc_auc", "f1"],
    return_train_score=True
)
print()
for metric in ["accuracy", "roc_auc", "f1"]:
    train_mean = results_cv[f"train_{metric}"].mean()
    test_mean  = results_cv[f"test_{metric}"].mean()
    print(f"{metric:10}: Train={train_mean:.4f} | Test={test_mean:.4f}")

# %% [markdown]
# ## 5.2 Learning Curves — Chẩn Đoán Overfitting/Underfitting

# %%
from sklearn.model_selection import learning_curve

def plot_learning_curve(model, X, y, title="Learning Curve", cv=5):
    train_sizes, train_scores, test_scores = learning_curve(
        model, X, y,
        train_sizes=np.linspace(0.1, 1.0, 10),
        cv=cv,
        scoring="accuracy",
        n_jobs=-1
    )
    train_mean = train_scores.mean(axis=1)
    train_std  = train_scores.std(axis=1)
    test_mean  = test_scores.mean(axis=1)
    test_std   = test_scores.std(axis=1)

    plt.figure(figsize=(8, 5))
    plt.plot(train_sizes, train_mean, "b-o", label="Train score")
    plt.fill_between(train_sizes,
                     train_mean - train_std, train_mean + train_std,
                     alpha=0.15, color="blue")
    plt.plot(train_sizes, test_mean, "r-o", label="Validation score")
    plt.fill_between(train_sizes,
                     test_mean - test_std, test_mean + test_std,
                     alpha=0.15, color="red")
    plt.title(title)
    plt.xlabel("Training set size")
    plt.ylabel("Score")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Chẩn đoán
    gap = train_mean[-1] - test_mean[-1]
    if train_mean[-1] < 0.85:
        print("⚠️  UNDERFITTING: Train score thấp → model quá đơn giản")
    elif gap > 0.1:
        print("⚠️  OVERFITTING: Gap lớn → model quá phức tạp")
    else:
        print("✅ Model cân bằng tốt!")

plot_learning_curve(
    RandomForestClassifier(n_estimators=100, random_state=42),
    X_clf, y_clf,
    title="Random Forest — Learning Curve"
)

# %% [markdown]
# ## 5.3 Confusion Matrix Sâu Hơn

# %%
from sklearn.metrics import ConfusionMatrixDisplay

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Confusion matrix số lượng
ConfusionMatrixDisplay.from_predictions(
    y_test_clf, rf_clf.predict(X_test_clf),
    display_labels=data_bc.target_names,
    ax=axes[0], colorbar=False, cmap="Blues"
)
axes[0].set_title("Confusion Matrix (Số lượng)")

# Confusion matrix tỉ lệ (normalize)
ConfusionMatrixDisplay.from_predictions(
    y_test_clf, rf_clf.predict(X_test_clf),
    display_labels=data_bc.target_names,
    normalize="true",   # chia theo hàng → tỉ lệ
    ax=axes[1], colorbar=False, cmap="Blues"
)
axes[1].set_title("Confusion Matrix (Tỉ lệ %)")

plt.tight_layout()
plt.show()


# ===========================================================================
# PHẦN 6: HYPERPARAMETER TUNING
# ===========================================================================

# %% [markdown]
# ## 6.1 GridSearchCV — Tìm Kiếm Toàn Diện

# %%
from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators":     [100, 200, 300],
    "max_depth":        [None, 5, 10, 15],
    "min_samples_leaf": [1, 5, 10],
    "max_features":     ["sqrt", "log2"]
}
# Tổng: 3×4×3×2 = 72 tổ hợp × 5-fold CV = 360 lần train!

rf_gs = RandomForestClassifier(random_state=42, n_jobs=-1)

grid_search = GridSearchCV(
    rf_gs,
    param_grid,
    cv=5,
    scoring="f1",           # tối ưu F1
    n_jobs=-1,
    verbose=1,
    return_train_score=True
)
grid_search.fit(X_train_clf, y_train_clf)

print(f"Best params: {grid_search.best_params_}")
print(f"Best CV F1:  {grid_search.best_score_:.4f}")
print(f"Test F1:     {f1_score(y_test_clf, grid_search.best_estimator_.predict(X_test_clf)):.4f}")

# Xem kết quả tất cả tổ hợp
cv_results_df = pd.DataFrame(grid_search.cv_results_)
cv_results_df = cv_results_df.sort_values("mean_test_score", ascending=False)
print("\nTop 5 tổ hợp tham số:")
print(cv_results_df[["params", "mean_test_score", "std_test_score"]].head())

# %% [markdown]
# ## 6.2 RandomizedSearchCV — Tìm Kiếm Ngẫu Nhiên (Hiệu Quả Hơn)

# %%
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_dist = {
    "n_estimators":     randint(50, 500),   # 50 đến 500 ngẫu nhiên
    "max_depth":        [None, 5, 10, 15, 20, 30],
    "min_samples_leaf": randint(1, 20),
    "max_features":     ["sqrt", "log2", 0.3, 0.5],
    "bootstrap":        [True, False]
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42, n_jobs=-1),
    param_dist,
    n_iter=50,          # thử 50 tổ hợp ngẫu nhiên (thay vì 360 của Grid)
    cv=5,
    scoring="f1",
    n_jobs=-1,
    verbose=1,
    random_state=42
)
random_search.fit(X_train_clf, y_train_clf)

print(f"Best params: {random_search.best_params_}")
print(f"Best CV F1:  {random_search.best_score_:.4f}")

# +--------------------------+------------------+----------------------+
# |                          | GridSearchCV     | RandomizedSearchCV   |
# +--------------------------+------------------+----------------------+
# | Không gian tham số       | Nhỏ (<100 tổ hợp)| Lớn (>100 tổ hợp)  |
# | Tốc độ                   | Chậm             | Nhanh                |
# | Đảm bảo tìm best         | ✅ Có            | ❌ Không             |
# | Thực tế hay dùng         | Tinh chỉnh cuối  | Khám phá ban đầu    |
# +--------------------------+------------------+----------------------+
#
# 💡 Chiến lược tối ưu:
# RandomizedSearch (không gian lớn) → tìm vùng tốt
# GridSearch (không gian nhỏ hơn trong vùng đó) → tinh chỉnh


# ===========================================================================
# PHẦN 7: SKLEARN PIPELINES
# ===========================================================================

# %% [markdown]
# ## 7.1 Tại Sao Cần Pipeline?
#
# VẤN ĐỀ KHÔNG CÓ PIPELINE (DATA LEAKAGE!):
#
#   ❌ SAI — scaler fit trên toàn bộ data (kể cả test):
#      scaler.fit_transform(X)   → thấy test set trước → data leakage!
#
#   ❌ SAI — phải lặp lại preprocessing mỗi lần:
#      scaler.fit_transform(X_train)
#      imputer.fit_transform(...)
#      ... và predict cũng phải lặp lại!
#
#   ✅ ĐÚNG — dùng Pipeline: tất cả trong 1 object

# %% [markdown]
# ## 7.2 ColumnTransformer — Xử Lý Nhiều Loại Cột

# %%
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

# Dataset có cả số và categorical
np.random.seed(42)
n_records = 200
df_mixed = pd.DataFrame({
    "Tuoi":     np.random.randint(22, 55, n_records).astype(float),
    "Luong":    np.random.normal(18, 5, n_records),
    "NamKN":    np.random.randint(0, 20, n_records).astype(float),
    "Phong":    np.random.choice(["IT", "KD", "HR"], n_records),
    "CapBac":   np.random.choice(["Junior", "Mid", "Senior"], n_records),
    "Churn":    np.random.randint(0, 2, n_records)
})

# Thêm một số NaN
df_mixed.loc[np.random.choice(n_records, 20), "Tuoi"]  = np.nan
df_mixed.loc[np.random.choice(n_records, 15), "Luong"] = np.nan
df_mixed.loc[np.random.choice(n_records, 10), "Phong"] = np.nan

X_m = df_mixed.drop("Churn", axis=1)
y_m = df_mixed["Churn"]

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X_m, y_m, test_size=0.2, stratify=y_m, random_state=42
)

# Định nghĩa cột theo loại
num_features_m = ["Tuoi", "Luong", "NamKN"]
cat_features_m = ["Phong", "CapBac"]

# Preprocessing cho cột số
num_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),  # điền median cho NaN
    ("scaler",  StandardScaler())                    # rồi scale
])

# Preprocessing cho cột categorical
cat_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),    # điền mode
    ("onehot",  OneHotEncoder(handle_unknown="ignore", drop="first"))
])

# Gộp lại bằng ColumnTransformer
preprocessor = ColumnTransformer([
    ("num", num_transformer, num_features_m),
    ("cat", cat_transformer, cat_features_m),
])

# Full Pipeline: preprocessing + model
full_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier",   RandomForestClassifier(n_estimators=100, random_state=42))
])

# Fit và predict — CHỈ 1 DÒNG!
full_pipeline.fit(X_train_m, y_train_m)
print(f"Test Accuracy: {full_pipeline.score(X_test_m, y_test_m):.4f}")

# Predict trực tiếp với raw data (không cần transform thủ công)
y_pred_full = full_pipeline.predict(X_test_m)

# %% [markdown]
# ## 7.3 Pipeline với GridSearchCV

# %%
# Pipeline hoạt động hoàn hảo với GridSearch
param_grid_pipe = {
    "classifier__n_estimators":  [100, 200],
    "classifier__max_depth":     [None, 10],
    "preprocessor__num__imputer__strategy": ["mean", "median"]
    # Tên param: tên_bước__tham_số
}

grid_pipe = GridSearchCV(full_pipeline, param_grid_pipe, cv=5, scoring="f1", n_jobs=-1)
grid_pipe.fit(X_train_m, y_train_m)
print(f"Best params: {grid_pipe.best_params_}")
print(f"Test F1:     {f1_score(y_test_m, grid_pipe.best_estimator_.predict(X_test_m)):.4f}")


# ===========================================================================
# PHẦN 8: UNSUPERVISED LEARNING
# ===========================================================================

# %% [markdown]
# ## 8.1 K-Means Clustering
#
# Chia data thành K nhóm sao cho:
# → Các điểm cùng nhóm gần nhau nhất
# → Các điểm khác nhóm xa nhau nhất
#
# Thuật toán:
#   1. Khởi tạo K điểm trung tâm (centroid) ngẫu nhiên
#   2. Gán mỗi điểm vào centroid gần nhất
#   3. Tính lại centroid = trung bình của nhóm
#   4. Lặp lại 2-3 cho đến khi centroid không đổi

# %%
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Dataset: phân khúc khách hàng
np.random.seed(42)
n_cust = 300
df_khach = pd.DataFrame({
    "TuoiKH":       np.random.randint(18, 65, n_cust),
    "ThuNhap":      np.random.normal(25, 8, n_cust).clip(8, 60),
    "DiemTieuDung": np.random.randint(1, 100, n_cust)
})

X_km = df_khach.values
scaler_km = StandardScaler()
X_km_scaled = scaler_km.fit_transform(X_km)

# --- Chọn K tối ưu: Elbow Method + Silhouette ---
inertias, silhouettes_km = [], []
K_range = range(2, 11)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels_km = km.fit_predict(X_km_scaled)
    inertias.append(km.inertia_)
    silhouettes_km.append(silhouette_score(X_km_scaled, labels_km))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(K_range, inertias, "b-o", ms=6)
ax1.set_title("Elbow Method — Tìm K tối ưu")
ax1.set_xlabel("Số cluster K")
ax1.set_ylabel("Inertia")
# "Khuỷu tay" (elbow) = điểm inertia giảm chậm lại → K tối ưu

ax2.plot(K_range, silhouettes_km, "r-o", ms=6)
ax2.set_title("Silhouette Score")
ax2.set_xlabel("Số cluster K")
ax2.set_ylabel("Silhouette Score (cao hơn = tốt hơn)")

plt.tight_layout()
plt.show()

best_k = list(K_range)[np.argmax(silhouettes_km)]
print(f"K tối ưu theo Silhouette: {best_k}")

# Phân cụm với K tối ưu
km_final = KMeans(n_clusters=best_k, random_state=42, n_init=10)
df_khach["Cluster"] = km_final.fit_predict(X_km_scaled)

print("\nĐặc điểm từng phân khúc khách hàng:")
print(df_khach.groupby("Cluster")[["TuoiKH", "ThuNhap", "DiemTieuDung"]].mean().round(1))

# Visualize
fig, ax = plt.subplots(figsize=(8, 5))
colors_km = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12"]
for c in df_khach["Cluster"].unique():
    mask = df_khach["Cluster"] == c
    ax.scatter(df_khach.loc[mask, "ThuNhap"],
               df_khach.loc[mask, "DiemTieuDung"],
               c=colors_km[c % len(colors_km)], alpha=0.7, s=40,
               label=f"Nhóm {c}")

centroids_original = scaler_km.inverse_transform(km_final.cluster_centers_)
ax.scatter(centroids_original[:, 1], centroids_original[:, 2],
           c="black", marker="X", s=200, zorder=5, label="Centroids")
ax.set_xlabel("Thu nhập (triệu)")
ax.set_ylabel("Điểm tiêu dùng")
ax.set_title("Phân khúc khách hàng (K-Means)")
ax.legend()
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 8.2 DBSCAN — Clustering Không Cần Biết K
#
# Ưu điểm DBSCAN:
#   → Không cần chỉ định K trước
#   → Tìm được cluster hình dạng bất kỳ (không chỉ hình cầu)
#   → Tự xác định outliers (điểm -1)
#
# Nhược điểm:
#   → Khó tune eps và min_samples
#   → Không tốt với dữ liệu high-dimensional

# %%
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.5, min_samples=10)
labels_db = dbscan.fit_predict(X_km_scaled)

n_clusters_db = len(set(labels_db)) - (1 if -1 in labels_db else 0)
n_outliers_db  = (labels_db == -1).sum()
print(f"Số cluster tìm được: {n_clusters_db}")
print(f"Số outliers: {n_outliers_db}")

# %% [markdown]
# ## 8.3 PCA — Giảm Chiều Dữ Liệu
#
# Tại sao cần giảm chiều?
# Dataset với 100 features:
#   → Khó visualize
#   → Nhiều features thừa, tương quan cao
#   → Model có thể overfit (curse of dimensionality)
#
# PCA (Principal Component Analysis):
#   → Tìm các "hướng" chứa nhiều thông tin nhất trong data
#   → Giữ lại N hướng quan trọng nhất
#   → Giảm từ 100 features xuống 5-10 mà giữ 90%+ thông tin

# %%
from sklearn.decomposition import PCA

# Scale trước PCA (bắt buộc!)
scaler_pca = StandardScaler()
X_bc_scaled_pca = scaler_pca.fit_transform(X_clf)

# PCA: giải thích variance
pca_full = PCA()
pca_full.fit(X_bc_scaled_pca)

# Cumulative explained variance
cum_var = np.cumsum(pca_full.explained_variance_ratio_)

plt.figure(figsize=(9, 4))
plt.subplot(1, 2, 1)
plt.bar(range(1, 11), pca_full.explained_variance_ratio_[:10] * 100,
        color="steelblue")
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance (%)")
plt.title("Variance mỗi component")

plt.subplot(1, 2, 2)
plt.plot(range(1, 21), cum_var[:20] * 100, "b-o", ms=4)
plt.axhline(90, color="red", ls="--", label="90% threshold")
plt.xlabel("Số components")
plt.ylabel("Cumulative Variance (%)")
plt.title("Giữ bao nhiêu component?")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

n_components_90 = np.argmax(cum_var >= 0.90) + 1
print(f"Components để giữ 90% variance: {n_components_90}/{X_clf.shape[1]}")

# PCA để visualize (2D)
pca_2d = PCA(n_components=2)
X_bc_2d = pca_2d.fit_transform(X_bc_scaled_pca)

plt.figure(figsize=(8, 5))
for label, name, color in zip([0,1], data_bc.target_names, ["#e74c3c","#2ecc71"]):
    mask = y_clf == label
    plt.scatter(X_bc_2d[mask, 0], X_bc_2d[mask, 1],
                c=color, alpha=0.7, s=30, label=name)
plt.xlabel(f"PC1 ({pca_2d.explained_variance_ratio_[0]*100:.1f}%)")
plt.ylabel(f"PC2 ({pca_2d.explained_variance_ratio_[1]*100:.1f}%)")
plt.title("Breast Cancer: PCA 2D Visualization")
plt.legend()
plt.tight_layout()
plt.show()

# PCA trong Pipeline
from sklearn.svm import SVC

pipe_pca = Pipeline([
    ("scaler", StandardScaler()),
    ("pca",    PCA(n_components=n_components_90)),
    ("svm",    SVC(kernel="rbf", random_state=42))
])
cv_pca = cross_val_score(pipe_pca, X_clf, y_clf, cv=5, scoring="accuracy")
print(f"\nSVM + PCA ({n_components_90} components) CV Accuracy: {cv_pca.mean():.4f}")

# %% [markdown]
# ## 8.4 t-SNE — Visualization Mạnh Mẽ Hơn
#
# t-SNE: phi tuyến, tốt hơn PCA để visualize cluster
# ⚠️ Chỉ dùng để visualize, KHÔNG dùng để giảm chiều trước training!

# %%
from sklearn.manifold import TSNE

tsne = TSNE(
    n_components=2,
    perplexity=30,     # số hàng xóm (thường 5-50)
    random_state=42,
    n_iter=1000
)
X_bc_tsne = tsne.fit_transform(X_bc_scaled_pca)

plt.figure(figsize=(8, 5))
for label, name, color in zip([0,1], data_bc.target_names, ["#e74c3c","#2ecc71"]):
    mask = y_clf == label
    plt.scatter(X_bc_tsne[mask, 0], X_bc_tsne[mask, 1],
                c=color, alpha=0.7, s=30, label=name)
plt.title("Breast Cancer: t-SNE Visualization")
plt.legend()
plt.axis("off")
plt.tight_layout()
plt.show()


# ===========================================================================
# PHẦN 9: PROJECT THỰC TẾ — DỰ ĐOÁN GIÁ NHÀ CALIFORNIA
# ===========================================================================

# %% [markdown]
# ## 9.1 Full Workflow hoàn chỉnh
#
# Áp dụng toàn bộ workflow từ Phần 1-8 vào 1 bài toán hoàn chỉnh.
#
# Bài toán: Dự đoán giá nhà California
# Dataset:  sklearn.datasets.fetch_california_housing
# Metric:   RMSE (regression)

# %%
import seaborn as sns
from scipy.stats import randint as sp_randint
import warnings
warnings.filterwarnings("ignore")

sns.set_theme(style="whitegrid")

# ============================================================
# BƯỚC 1: TẢI DỮ LIỆU & EDA
# ============================================================
housing_proj = fetch_california_housing(as_frame=True)
df_proj = housing_proj.frame

print("=== THÔNG TIN DATASET ===")
print(f"Shape: {df_proj.shape}")
print(f"\nMissing values:\n{df_proj.isnull().sum()}")
print(f"\nThống kê:\n{df_proj.describe().T.round(2)}")

# Phân phối target
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
df_proj["MedHouseVal"].hist(bins=50, ax=axes[0], color="steelblue")
axes[0].set_title("Phân phối Giá Nhà")
axes[0].set_xlabel("Giá ($100K)")

np.log1p(df_proj["MedHouseVal"]).hist(bins=50, ax=axes[1], color="steelblue")
axes[1].set_title("Phân phối Giá Nhà (log scale)")
axes[1].set_xlabel("log(Giá)")
plt.tight_layout()
plt.show()

# ============================================================
# BƯỚC 2: FEATURE ENGINEERING
# ============================================================
df_proj["RoomsPerHousehold"]     = df_proj["AveRooms"]    / df_proj["HouseAge"].clip(1)
df_proj["BedroomsPerRoom"]       = df_proj["AveBedrms"]   / df_proj["AveRooms"].clip(1)
df_proj["PopulationPerHousehold"]= df_proj["Population"]  / df_proj["AveOccup"].clip(1)

X_proj = df_proj.drop("MedHouseVal", axis=1)
y_proj = df_proj["MedHouseVal"]

# ============================================================
# BƯỚC 3: CHIA DỮ LIỆU
# ============================================================
X_train_proj, X_test_proj, y_train_proj, y_test_proj = train_test_split(
    X_proj, y_proj, test_size=0.2, random_state=42
)
print(f"\nTrain: {X_train_proj.shape[0]} | Test: {X_test_proj.shape[0]}")

# ============================================================
# BƯỚC 4: TẠO PIPELINE
# ============================================================
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

preprocessor_proj = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler",  StandardScaler())
])

# ============================================================
# BƯỚC 5: HUẤN LUYỆN & SO SÁNH MODELS (Baseline)
# ============================================================
models_proj = {
    "Linear Regression": Pipeline([("prep", preprocessor_proj), ("model", LinearRegression())]),
    "Ridge":             Pipeline([("prep", preprocessor_proj), ("model", Ridge(alpha=1.0))]),
    "Random Forest":     Pipeline([("prep", preprocessor_proj),
                                   ("model", RandomForestRegressor(n_estimators=100,
                                                                    random_state=42, n_jobs=-1))]),
}

print("\n=== SO SÁNH MODELS (5-fold CV) ===")
results_proj = {}
for name, pipe in models_proj.items():
    cv_scores_proj = cross_val_score(pipe, X_train_proj, y_train_proj,
                                      cv=5, scoring="neg_root_mean_squared_error",
                                      n_jobs=-1)
    rmse_mean = -cv_scores_proj.mean()
    rmse_std  = cv_scores_proj.std()
    results_proj[name] = {"RMSE Mean": rmse_mean, "RMSE Std": rmse_std}
    print(f"{name:20}: RMSE = {rmse_mean:.4f} ± {rmse_std:.4f}")

# ============================================================
# BƯỚC 6: TINH CHỈNH MODEL TỐT NHẤT
# ============================================================
param_dist_proj = {
    "model__n_estimators":     sp_randint(100, 500),
    "model__max_depth":        [None, 10, 20, 30],
    "model__min_samples_leaf": sp_randint(1, 10),
    "model__max_features":     ["sqrt", 0.3, 0.5]
}
rf_pipe_proj = Pipeline([
    ("prep",  preprocessor_proj),
    ("model", RandomForestRegressor(random_state=42, n_jobs=-1))
])
random_search_proj = RandomizedSearchCV(
    rf_pipe_proj, param_dist_proj, n_iter=30, cv=5,
    scoring="neg_root_mean_squared_error",
    random_state=42, n_jobs=-1, verbose=0
)
random_search_proj.fit(X_train_proj, y_train_proj)
print(f"\nBest params: {random_search_proj.best_params_}")
print(f"Best CV RMSE: {-random_search_proj.best_score_:.4f}")

# ============================================================
# BƯỚC 7: ĐÁNH GIÁ TRÊN TEST SET (LẦN CUỐI)
# ============================================================
best_model_proj = random_search_proj.best_estimator_
y_pred_final = best_model_proj.predict(X_test_proj)

rmse_final = np.sqrt(mean_squared_error(y_test_proj, y_pred_final))
mae_final  = mean_absolute_error(y_test_proj, y_pred_final)
r2_final   = r2_score(y_test_proj, y_pred_final)

print("\n=== KẾT QUẢ CUỐI CÙNG (Test Set) ===")
print(f"RMSE: {rmse_final:.4f} (×$100K) = sai số trung bình ~${rmse_final*100000:,.0f}")
print(f"MAE:  {mae_final:.4f}")
print(f"R²:   {r2_final:.4f} → Model giải thích {r2_final*100:.1f}% variance")

# Visualize kết quả cuối
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].scatter(y_test_proj, y_pred_final, alpha=0.3, s=15, color="steelblue")
axes[0].plot([y_test_proj.min(), y_test_proj.max()],
             [y_test_proj.min(), y_test_proj.max()], "r--", linewidth=2)
axes[0].set_xlabel("Giá thực tế")
axes[0].set_ylabel("Giá dự đoán")
axes[0].set_title(f"Predicted vs Actual (R²={r2_final:.3f})")

residuals = y_test_proj - y_pred_final
axes[1].hist(residuals, bins=50, color="steelblue", edgecolor="white")
axes[1].axvline(0, color="red", ls="--", linewidth=2)
axes[1].set_xlabel("Sai số (Actual - Predicted)")
axes[1].set_ylabel("Số lượng")
axes[1].set_title("Phân phối sai số (Residuals)")

plt.suptitle("Kết Quả Dự Đoán Giá Nhà — Random Forest", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()

# Feature Importance
rf_final = best_model_proj.named_steps["model"]
fi_proj = pd.Series(rf_final.feature_importances_, index=X_proj.columns)
fi_proj_sorted = fi_proj.sort_values(ascending=False).head(10)

plt.figure(figsize=(9, 5))
fi_proj_sorted.plot(kind="barh", color="steelblue")
plt.xlabel("Importance")
plt.title("Top 10 Features Quan Trọng Nhất")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# ============================================================
# BƯỚC 8: LƯU MODEL
# ============================================================
import joblib
joblib.dump(best_model_proj, "housing_model.pkl")
print("\n✅ Model đã được lưu: housing_model.pkl")

# Tải lại và predict
loaded_model = joblib.load("housing_model.pkl")
sample = X_test_proj.iloc[:3]
print(f"\nDự đoán giá 3 căn nhà đầu tiên ($100K):")
print(loaded_model.predict(sample).round(3))
print(f"Giá thực tế:")
print(y_test_proj.iloc[:3].values)


# ===========================================================================
# PHẦN 10: LỘ TRÌNH HỌC TIẾP
# ===========================================================================

# %% [markdown]
# ## ✅ Đã nắm vững sau file này:
#
#   → Supervised Learning: Regression + Classification
#   → Các mô hình: Linear, Ridge/Lasso, Trees, RF, GBM, SVM, KNN, NB
#   → Model Evaluation: Cross-validation, metrics
#   → Hyperparameter Tuning: Grid/RandomizedSearch
#   → Pipelines chuẩn công nghiệp
#   → Unsupervised: K-Means, DBSCAN, PCA, t-SNE
#   → End-to-end project workflow
#
# ## Level 1 — Consolidation (1-2 tháng):
#   1. Kaggle Getting Started:
#      → Titanic (classification)
#      → House Prices (regression)
#      → Mục tiêu: top 25%
#   2. Thực hành với real datasets (UCI ML Repository, Kaggle)
#   3. Feature Engineering: Polynomial, Interaction, Target encoding
#
# ## Level 2 — Advanced Classical ML (1-2 tháng):
#   4. Ensemble Methods: Stacking, Blending, Voting Classifier
#   5. Interpretability: SHAP values (pip install shap), LIME
#   6. Time Series: statsmodels (ARIMA), Prophet
#
# ## Level 3 — Deep Learning (2-3 tháng):
#   7. TensorFlow/Keras hoặc PyTorch
#      → Dense networks (tabular data)
#      → Convolutional (ảnh)
#      → Recurrent/LSTM (chuỗi thời gian)
#   8. Sách: "Hands-On ML" Ch.10-19, "Deep Learning with Python" (Chollet)
#
# ## Level 4 — Production ML (Song song với Level 2-3):
#   9. MLflow: theo dõi experiments
#   10. FastAPI: deploy model thành API
#   11. Docker: đóng gói model
#   12. GitHub Actions: CI/CD cho ML


# ===========================================================================
# CHEAT SHEET — QUICK REFERENCE
# ===========================================================================

# %% [markdown]
# ## Chọn Mô Hình
#
# DỮ LIỆU DẠNG BẢNG (tabular):
#   → Bắt đầu: LinearRegression / LogisticRegression (baseline)
#   → Mạnh:    RandomForest → XGBoost/LightGBM (state-of-the-art)
#
# DỮ LIỆU ÍT, CẦN GIẢI THÍCH:
#   → LinearRegression + Ridge/Lasso
#   → LogisticRegression
#
# DỮ LIỆU LỚN, MUỐN ACCURACY CAO NHẤT:
#   → XGBoost / LightGBM
#   → Neural Networks (nếu >100K mẫu)
#
# VĂN BẢN / ÂM THANH / ẢNH:
#   → Deep Learning (file tiếp theo)

# %%
# ============================================================
# SKLEARN WORKFLOW TEMPLATE
# ============================================================

# 1. Import
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# 2. Split
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, stratify=y, random_state=42
# )

# 3. Pipeline
# pipe = Pipeline([
#     ("scaler", StandardScaler()),
#     ("model",  RandomForestClassifier())
# ])

# 4. CV
# cv_score = cross_val_score(pipe, X_train, y_train, cv=5, scoring="f1").mean()

# 5. Fit & Evaluate
# pipe.fit(X_train, y_train)
# y_pred = pipe.predict(X_test)

# ============================================================
# METRICS QUICK REFERENCE
# ============================================================
# +---------------+----------------+-------------------------------------+
# | Task          | Metric         | Code                                |
# +---------------+----------------+-------------------------------------+
# | Regression    | RMSE           | np.sqrt(mean_squared_error(y, yp))  |
# | Regression    | MAE            | mean_absolute_error(y, yp)          |
# | Regression    | R²             | r2_score(y, yp)                     |
# | Classification| Accuracy       | accuracy_score(y, yp)               |
# | Classification| F1             | f1_score(y, yp)                     |
# | Classification| ROC-AUC        | roc_auc_score(y, yp_proba)          |
# | Imbalanced    | F1 macro       | f1_score(y, yp, average="macro")    |
# +---------------+----------------+-------------------------------------+

# ============================================================
# HYPERPARAMETER QUICK REFERENCE
# ============================================================
# +---------------+------------------------------+---------------------------+
# | Model         | Params quan trọng            | Gợi ý bắt đầu            |
# +---------------+------------------------------+---------------------------+
# | Ridge/Lasso   | alpha                        | 0.001 → 1000 (log scale)  |
# | Random Forest | n_estimators, max_depth,     | 100-500, None/10/20, 1-10 |
# |               | min_samples_leaf             |                           |
# | XGBoost       | learning_rate, n_estimators, | 0.01-0.3, 100-1000, 3-8   |
# |               | max_depth                    |                           |
# | SVM           | C, gamma                     | 0.1-100, "scale"/"auto"   |
# | KNN           | n_neighbors                  | 1-30                      |
# +---------------+------------------------------+---------------------------+

# ============================================================
# CHECKLIST DỰ ÁN ML
# ============================================================
checklist = """
□ 1.  Định nghĩa bài toán — Regression hay Classification? Metric nào?
□ 2.  EDA — phân phối, missing, outliers, tương quan
□ 3.  Train/Test split TRƯỚC khi làm bất cứ gì (stratify nếu classification)
□ 4.  Pipeline: Imputer → Scaler → Encoder → Model
□ 5.  Baseline model (Linear/Logistic) làm tham chiếu
□ 6.  Cross-validation — không dùng test set đến bước cuối!
□ 7.  Thử 3-5 models khác nhau
□ 8.  Hyperparameter tuning model tốt nhất
□ 9.  Evaluate trên test set 1 lần duy nhất
□ 10. Visualize kết quả + feature importance
□ 11. Lưu model với joblib
□ 12. Viết tóm tắt: model chọn, lý do, limitations
"""
print(checklist)

# ============================================================
# TÀI NGUYÊN KHUYẾN NGHỊ
# ============================================================
# +----------------------------+----------------+--------------------------+
# | Tài nguyên                 | Loại           | Link                     |
# +----------------------------+----------------+--------------------------+
# | Stanford CS229             | Course miễn phí| cs229.stanford.edu       |
# | Harvard CS109x             | Course miễn phí| edX                      |
# | Hands-On ML (Géron)        | Sách thực hành | ageron/handson-ml3       |
# | ISL                        | Sách học thuật | statlearning.com         |
# | fast.ai                    | Course thực chiến| fast.ai                |
# | Kaggle Learn               | Ngắn, thực hành| kaggle.com/learn         |
# +----------------------------+----------------+--------------------------+

print("\n🎉 Hoàn thành file Machine Learning với Python!")
print("📚 Sách khuyên đọc: Hands-On ML — Aurélien Géron (github.com/ageron/handson-ml3)")
print("🎓 Course: Stanford CS229 · Harvard CS109x · fast.ai")
print("💻 Thực hành: kaggle.com/competitions")