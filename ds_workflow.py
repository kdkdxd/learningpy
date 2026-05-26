# REAL-WORLD DATA SCIENTIST WORKFLOW
# Bài toán: Dự đoán khách hàng có rời bỏ dịch vụ không (Churn)
# Đây là bài toán classification phổ biến nhất trong industry

#  [PHẦN 1] IMPORT THƯ VIỆN 
# Data Scientist dùng rất nhiều thư viện chuyên biệt

import pandas as pd          # Xử lý dữ liệu dạng bảng (DataFrame)
import numpy as np           # Tính toán số học, array operations
import matplotlib.pyplot as plt  # Vẽ biểu đồ cơ bản
import seaborn as sns        # Vẽ biểu đồ thống kê đẹp hơn

from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
# train_test_split   → chia data thành tập train và test
# cross_val_score    → đánh giá model bằng cross-validation (kỹ hơn)
# StratifiedKFold    → giữ tỉ lệ class khi chia fold (quan trọng khi data imbalanced)

from sklearn.preprocessing import StandardScaler, LabelEncoder
# StandardScaler     → chuẩn hóa feature về mean=0, std=1
# LabelEncoder       → chuyển categorical (VD: "Yes"/"No") thành số (1/0)

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
# Đây là 2 thuật toán mạnh nhất cho tabular data trong thực tế

from sklearn.linear_model import LogisticRegression
# Model đơn giản nhưng interpretable — thường dùng làm baseline

from sklearn.metrics import (
    classification_report,   # Báo cáo đầy đủ: precision, recall, F1
    confusion_matrix,        # Ma trận nhầm lẫn
    roc_auc_score,           # AUC-ROC score — metric quan trọng nhất cho imbalanced data
    roc_curve                # Dữ liệu để vẽ đường ROC curve
)

from sklearn.pipeline import Pipeline
# Pipeline → gộp các bước preprocessing + model thành 1 object
# Lý do: tránh data leakage, code gọn hơn, dễ deploy

import warnings
warnings.filterwarnings('ignore')  # Tắt warnings không cần thiết khi chạy thực tế

print("✅ Tất cả thư viện đã được import thành công")
print("=" * 60)


# [PHẦN 2] TẠO DỮ LIỆU GIẢ LẬP THỰC TẾ 
# Trong thực tế: đọc từ SQL database, CSV, Parquet, API
# Ở đây ta tạo data giả để chạy được ngay

np.random.seed(42)  # Fix seed để kết quả reproducible — rất quan trọng trong DS
n_customers = 5000  # 5000 khách hàng — quy mô nhỏ nhưng đủ để demo

# Tạo DataFrame với các feature thực tế của bài toán churn
data = pd.DataFrame({
    'customer_id': range(1, n_customers + 1),

    # Demographic features
    'age': np.random.randint(18, 70, n_customers),
    'gender': np.random.choice(['Male', 'Female'], n_customers),

    # Account features
    'tenure_months': np.random.randint(1, 72, n_customers),  # Số tháng dùng dịch vụ
    'contract_type': np.random.choice(
        ['Month-to-Month', 'One Year', 'Two Year'],
        n_customers,
        p=[0.55, 0.25, 0.20]   # Phân phối thực tế: hầu hết là monthly
    ),

    # Usage features
    'monthly_charges': np.random.uniform(20, 120, n_customers),
    'total_charges': np.random.uniform(100, 8000, n_customers),
    'num_products': np.random.randint(1, 6, n_customers),
    'support_calls': np.random.poisson(2, n_customers),  # Số lần gọi support

    # Service features
    'has_internet': np.random.choice(['Yes', 'No'], n_customers, p=[0.8, 0.2]),
    'payment_method': np.random.choice(
        ['Credit Card', 'Bank Transfer', 'Electronic Check', 'Mailed Check'],
        n_customers
    ),
})

# Tạo target variable (churn) — có logic thực tế
# Khách hàng có monthly contract và support nhiều → dễ churn hơn
churn_probability = (
    0.05  # Base rate
    + 0.25 * (data['contract_type'] == 'Month-to-Month')  # Monthly contract → rủi ro cao
    + 0.15 * (data['support_calls'] > 4)                  # Nhiều cuộc gọi support → không hài lòng
    + 0.10 * (data['tenure_months'] < 6)                  # Khách mới → dễ bỏ
    - 0.10 * (data['num_products'] > 3)                   # Nhiều sản phẩm → gắn bó hơn
)

# Thêm nhiễu ngẫu nhiên để realistic
churn_probability = churn_probability.clip(0.02, 0.85)
data['churn'] = np.random.binomial(1, churn_probability)

# Thêm missing values — thực tế LUÔN có missing data
missing_mask = np.random.random(n_customers) < 0.08  # 8% missing
data.loc[missing_mask, 'monthly_charges'] = np.nan
data.loc[np.random.random(n_customers) < 0.05, 'total_charges'] = np.nan

print(f"📊 Dataset shape: {data.shape}")
print(f"📊 Churn rate: {data['churn'].mean():.1%}")
print()


# [PHẦN 3] EXPLORATORY DATA ANALYSIS (EDA)
# Đây là phần Data Scientist dành nhiều thời gian NHẤT
# "Hiểu data trước khi model"

print("=" * 60)
print("📋 EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# 3.1 Thông tin tổng quan
print("\n[3.1] Tổng quan dataset:")
print(data.info())  # Kiểu dữ liệu từng cột, số non-null

# 3.2 Thống kê mô tả
print("\n[3.2] Thống kê mô tả (numerical features):")
print(data.describe().round(2))
# → Nhìn vào mean, std, min, max để phát hiện outliers

# 3.3 Kiểm tra missing values — LUÔN làm bước này đầu tiên
print("\n[3.3] Missing values:")
missing_info = data.isnull().sum()
missing_pct = (data.isnull().sum() / len(data) * 100).round(2)
missing_df = pd.DataFrame({
    'Missing Count': missing_info,
    'Missing %': missing_pct
}).query('`Missing Count` > 0')  # Chỉ hiện cột có missing
print(missing_df)

# 3.4 Phân phối target variable — kiểm tra class imbalance
print("\n[3.4] Phân phối Churn (target variable):")
churn_dist = data['churn'].value_counts(normalize=True)
print(churn_dist.rename({0: 'Không churn (0)', 1: 'Có churn (1)'}))
# → Nếu imbalanced (VD: 90% không churn) → phải xử lý đặc biệt

# 3.5 Correlation với target
print("\n[3.5] Tương quan của features với Churn:")
numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
numeric_cols.remove('customer_id')  # ID không có ý nghĩa thống kê
correlations = data[numeric_cols].corr()['churn'].drop('churn').sort_values(key=abs, ascending=False)
print(correlations.round(3))
# → Feature nào tương quan cao với target → likely important feature


# [PHẦN 4] XỬ LÝ DỮ LIỆU (DATA PREPROCESSING)
print("\n" + "=" * 60)
print("🔧 DATA PREPROCESSING")
print("=" * 60)

# 4.1 Tách features (X) và target (y)
# customer_id là identifier, không phải feature
X = data.drop(columns=['customer_id', 'churn'])
y = data['churn']
# y là Series với giá trị 0 (không churn) hoặc 1 (churn)

# 4.2 Phân loại feature types — quan trọng để xử lý đúng cách
categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
numerical_cols = X.select_dtypes(include=[np.number]).columns.tolist()

print(f"Categorical features: {categorical_cols}")
print(f"Numerical features: {numerical_cols}")

# 4.3 Xử lý Missing Values
# Chiến lược: median cho numerical (robust với outliers hơn mean)
for col in numerical_cols:
    median_val = X[col].median()
    X[col] = X[col].fillna(median_val)
    # Dùng median thay mean vì median không bị ảnh hưởng bởi outliers
    # VD: [1, 2, 3, 4, 1000] → mean=202, median=3

# 4.4 Encode Categorical Variables
# LabelEncoder chuyển text → số (vì ML model chỉ hiểu số)
le = LabelEncoder()
for col in categorical_cols: 
    X[col] = le.fit_transform(X[col])
    # "Male"/"Female" → 0/1
    # "Month-to-Month"/"One Year"/"Two Year" → 0/1/2

print(f"\n✅ Missing values sau xử lý: {X.isnull().sum().sum()}")

# 4.5 Train-Test Split — chia data TRƯỚC KHI scaling
# Lý do: tránh data leakage (test set không được "nhìn" thấy training data)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,          # 80% train, 20% test
    random_state=42,        # Reproducibility
    stratify=y              # Giữ nguyên tỉ lệ churn trong cả 2 set
)

print(f"\nTraining set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")
print(f"Churn rate - Train: {y_train.mean():.1%} | Test: {y_test.mean():.1%}")

# 4.6 Feature Scaling (Standardization)
# Nhiều model (Logistic Regression) yêu cầu features cùng scale
# RandomForest không cần, nhưng best practice vẫn scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
# fit_transform trên TRAIN: học mean & std từ training data
X_test_scaled = scaler.transform(X_test)
# transform trên TEST: dùng mean & std của training data (KHÔNG fit lại)
# → Đây là nguyên tắc quan trọng nhất để tránh data leakage


#  [PHẦN 5] TRAINING VÀ SO SÁNH MODELS
print("\n" + "=" * 60)
print("MODEL TRAINING & COMPARISON")
print("=" * 60)

# Thực tế: Data Scientist luôn thử nhiều model, không chỉ 1
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42)
    # n_jobs=-1 → dùng tất cả CPU cores để train nhanh hơn
}

results = {}  # Dict để lưu kết quả của từng model

for model_name, model in models.items():
    print(f"\n Training {model_name}...")

    # 5.1 Cross-Validation — đánh giá model đáng tin cậy hơn train/test split
    # StratifiedKFold: chia 5 fold, mỗi fold giữ tỉ lệ class
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(
        model, X_train_scaled, y_train,
        cv=cv,
        scoring='roc_auc',  # Dùng AUC vì data imbalanced
        n_jobs=-1
    )

    # 5.2 Train model trên toàn bộ training data
    model.fit(X_train_scaled, y_train)

    # 5.3 Predict trên test set
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
    # predict_proba → xác suất, cột [:, 1] là xác suất của class 1 (churn)
    # Quan trọng: dùng probability để tính AUC và ROC curve

    # 5.4 Tính metrics
    auc_score = roc_auc_score(y_test, y_pred_proba)

    results[model_name] = {
        'cv_auc_mean': cv_scores.mean(),
        'cv_auc_std': cv_scores.std(),
        'test_auc': auc_score,
        'model': model,
        'y_pred': y_pred,
        'y_pred_proba': y_pred_proba
    }

    print(f"   CV AUC: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")
    print(f"   Test AUC: {auc_score:.4f}")

# 5.5 In bảng so sánh
print("\n📊 So sánh tổng hợp:")
print(f"{'Model':<25} {'CV AUC':<15} {'Test AUC':<10}")
print("-" * 50)
for name, res in results.items():
    print(f"{name:<25} {res['cv_auc_mean']:.4f}±{res['cv_auc_std']:.4f}   {res['test_auc']:.4f}")


# [PHẦN 6] ĐÁNH GIÁ MODEL TỐT NHẤT CHI TIẾT
print("\n" + "=" * 60)
print("CHI TIẾT MODEL TỐT NHẤT")
print("=" * 60)

# Chọn model có test AUC cao nhất
best_model_name = max(results, key=lambda x: results[x]['test_auc'])
best = results[best_model_name]
print(f"\n🏆 Best model: {best_model_name} (AUC = {best['test_auc']:.4f})")

# 6.1 Classification Report
print("\n[6.1] Classification Report:")
print(classification_report(
    y_test, best['y_pred'],
    target_names=['Không churn', 'Có churn']
))
# Precision: trong số predicted churn, bao nhiêu % đúng thật?
# Recall:    trong số thật sự churn, model tìm được bao nhiêu %?
# F1-score:  harmonic mean của precision và recall
# → Business thường quan tâm Recall của class churn nhiều hơn

# 6.2 Confusion Matrix
print("[6.2] Confusion Matrix:")
cm = confusion_matrix(y_test, best['y_pred'])
print(f"                 Predicted: Không churn  |  Predicted: Churn")
print(f"Actual: Không churn       {cm[0][0]:>6}          |     {cm[0][1]:>6}")
print(f"Actual: Churn             {cm[1][0]:>6}          |     {cm[1][1]:>6}")
# TN (top-left):  Đúng — predict không churn, thật sự không churn
# FP (top-right): Sai — predict churn, thật sự không churn (False Alarm)
# FN (bottom-left): Sai — predict không churn, thật sự churn (Miss!)
# TP (bottom-right): Đúng — predict churn, thật sự churn


# [PHẦN 7] FEATURE IMPORTANCE
# "Feature nào quan trọng nhất?" — câu hỏi business LUÔN hỏi
print("\n" + "=" * 60)
print("🔍 FEATURE IMPORTANCE")
print("=" * 60)

if hasattr(best['model'], 'feature_importances_'):
    # Random Forest và Gradient Boosting có attribute này
    importances = pd.Series(
        best['model'].feature_importances_,
        index=X.columns
    ).sort_values(ascending=False)

    print("\nTop 8 features quan trọng nhất:")
    for feat, imp in importances.head(8).items():
        bar = "█" * int(imp * 100)  # Visual bar chart trong text
        print(f"  {feat:<20} {imp:.4f}  {bar}")


#[PHẦN 8] BUSINESS INSIGHT & ACTIONABLE OUTPUT
# Data Scientist thực tế phải đưa ra insight cho business
print("\n" + "=" * 60)
print("💼 BUSINESS INSIGHTS")
print("=" * 60)

# Tạo prediction cho toàn bộ data để phân tích
all_proba = best['model'].predict_proba(scaler.transform(X))[:, 1]
data_with_pred = data.copy()
data_with_pred['churn_probability'] = all_proba

# 8.1 Phân nhóm risk
# Business cần biết: khách nào cần can thiệp ngay?
data_with_pred['risk_segment'] = pd.cut(
    all_proba,
    bins=[0, 0.3, 0.6, 1.0],
    labels=['Low Risk', 'Medium Risk', 'High Risk']
)

print("\n[8.1] Phân phối Risk Segment:")
print(data_with_pred['risk_segment'].value_counts())

# 8.2 Khách hàng High Risk cần contact ngay
high_risk_customers = data_with_pred[
    data_with_pred['risk_segment'] == 'High Risk'
].sort_values('churn_probability', ascending=False)

print(f"\n[8.2] Top 5 khách hàng cần contact NGAY:")
print(high_risk_customers[['customer_id', 'churn_probability', 'contract_type', 'support_calls', 'tenure_months']].head())

# 8.3 Lưu kết quả ra file — để gửi cho business team
output_file = '/mnt/user-data/outputs/churn_predictions.csv'
high_risk_customers[['customer_id', 'churn_probability', 'risk_segment']].to_csv(
    output_file, index=False
)
print(f"\n✅ Predictions đã được lưu vào: {output_file}")


#[PHẦN 9] MODEL PERSISTENCE
# Lưu model để deploy lên production
import joblib  # Thư viện lưu/load Python objects

model_path = '/mnt/user-data/outputs/churn_model.pkl'
scaler_path = '/mnt/user-data/outputs/churn_scaler.pkl'

joblib.dump(best['model'], model_path)
joblib.dump(scaler, scaler_path)
print(f"\n✅ Model đã lưu: {model_path}")
print(f"✅ Scaler đã lưu: {scaler_path}")

# Cách load và dùng trong production:
# loaded_model = joblib.load('churn_model.pkl')
# loaded_scaler = joblib.load('churn_scaler.pkl')
# new_prediction = loaded_model.predict(loaded_scaler.transform(new_customer_data))


# [TỔNG KẾT]
print("\n" + "=" * 60)
print("✅ WORKFLOW HOÀN TẤT")
print("=" * 60)
print("""
Tóm tắt những gì một Data Scientist thực sự làm:

1. 📥 DATA INGESTION      — Load data từ database/file/API
2. 🔍 EDA                 — Hiểu data: missing values, distributions, correlations
3. 🔧 PREPROCESSING       — Clean data, encode categoricals, scale features
4. ✂️  TRAIN/TEST SPLIT   — Tách data đúng cách, tránh data leakage
5. 🤖 MODEL COMPARISON    — Thử nhiều model, dùng cross-validation
6. 📊 EVALUATION          — Dùng đúng metrics (AUC cho imbalanced data)
7. 🔍 FEATURE IMPORTANCE  — Giải thích model cho business
8. 💼 BUSINESS OUTPUT     — Đưa ra actionable insights
9. 💾 MODEL PERSISTENCE   — Lưu model để deploy production
""")
