
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import sys

sys.stdout.reconfigure(encoding="utf-8")

np.random.seed(170412)

print("==============Revise EDA==============")


employees1 = pd.read_csv("employees1.csv")


#G1 GENERAL LOOK
print("==================GENERAL LOOK==================")
print(f"Size: {employees1.shape[0]} rows {employees1.shape[1]} columns")
print(f"Dtypes: {employees1.dtypes}")
print(f"First 5 rows : {employees1.head()}")


#G2 MISSING VALUES
nanval = employees1.isna().sum()
nan_pct = (nanval/len(employees1)*100).round(2)
nan_report = pd.DataFrame({
    "NaN Quantity":nanval,
    "NaN Percentage":nan_pct
})
print(f"Nan Report : {nan_report}")

me_age = employees1["Age"].median()
me_salary = employees1["Salary"].median()
me_per = employees1["Performance"].median()

#FillNa
employees1["Age"]=employees1["Age"].fillna(me_age)
employees1["Salary"] = employees1["Salary"].fillna(me_salary)
employees1["Performance"] = employees1["Performance"].fillna(me_per)

cleaned_em = employees1
print(cleaned_em.head(7))

#seperate columns
num_cols = employees1.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = employees1.select_dtypes(include=object).columns.tolist()

#G3 Variables Distribution
n = len(num_cols)
if n > 0 :
    fig, axes = plt.subplots(1,n,figsize = (8*n,4), constrained_layout=True)
    if n == 1: axes = [axes]
    for ncol, ax  in zip(num_cols, axes) :
        sns.histplot(employees1[ncol], kde = True, color = "#63DAF8", bins = 20 , ax = ax)
        ax.axvline(employees1[ncol].mean(), color = "#F70C0C", ls = "-", lw = 0.7, label = "Mean")
        ax.axvline(employees1[ncol].median(), color = "#BA0BF4", ls = "--", lw = 0.7, label = "Median")
        ax.set_title(f"{ncol} Distribution", fontname = "Arial", fontsize = 17)
        ax.legend( fontsize = 9)
    plt.suptitle("Variables Distribution", fontname = "Arial", fontsize = 20, fontweight = "bold")
    plt.show


#G4 Salary Outliers
fig, ax = plt.subplots(figsize = (4,7))
sns.boxplot(employees1["Salary"], color = "#5AF043", flierprops = dict(marker="o", ms = 5, mfc = "#ED43F0", alpha = 0.65, label = "Outliers"))
ax.set_title("Salary Outliers", fontname = "Arial", fontsize = 20, fontweight = "bold")
ax.set_ylabel("Salary(VND)", fontname = "Arial", fontsize = 14)
ax.legend(fontsize = 9)
plt.tight_layout()
plt.show


# Heatmap Correlation between Age and Experience
corr = employees1[["Age","Experience"]].corr()
fig, ax = plt.subplots(figsize = (8,6))
mask = np.triu(np.ones_like(corr,dtype=bool))
sns.heatmap(corr, mask = mask, vmin = -1, vmax = 1, annot = True, cmap = "coolwarm", ax = ax, fmt = ".2f")
ax.set_title("Corr Matrix between Age & Exp", fontname = "Arial", fontsize = 16, fontweight = "bold")
plt.tight_layout()
plt.show()
r = corr.loc["Age", "Experience"]
if abs(r) >= 0.8:
    print(f"\nCorrelation between Age and Experience : corr = {r:.2f} => Strong Correlation")
elif abs(r) >= 0.3:
    print(f"\nCorrelation between Age and Experience : corr = {r:.2f} => Medium Correlation")
else:
    print(f"\nCorrelation between Age and Experience : corr = {r:.2f} => Weak Correlation")

top_pair = (corr.where(~mask).stack().reset_index().rename(columns={"level_0":"Val1","level_1":"Val2",0:"r"}))
print(f"\nStrongest Correlation :\n{top_pair}")


# Scatter Plot between Salary and Exp
fig, ax = plt.subplots(figsize = (6,5))
sns.despine()
sns.scatterplot(data = cleaned_em, x = cleaned_em["Experience"], y = cleaned_em["Salary"], marker="o", color = "#F27538", size = 4, edgecolor = "black",ax=ax, legend=False)
z = np.polyfit(cleaned_em["Experience"], cleaned_em["Salary"], 1)
p = np.poly1d(z)
x_line = np.linspace(1,35,350)
ax.plot(x_line, p(x_line), color = "#5E27F5", lw = 1.2, alpha = 0.7, label = "Trend line")
ax.set_title("Relationship between Salary and Exp", fontname = "Arial", fontsize = 18, fontweight = "bold")
ax.legend(fontsize = 10)
plt.tight_layout()
plt.show
# Salary According to Department

desa_stat = (cleaned_em.groupby("Department")["Salary"]
             .agg(["mean", "median", "std", "count"])
             .round(2)
             .sort_values("mean", ascending=False))

print(desa_stat)

fig,ax = plt.subplots(figsize = (9,6), constrained_layout=True)
sns.barplot( x = desa_stat.index, y = desa_stat["mean"], palette="Set1", edgecolor = "black", width=0.6, ax =ax)
for bar, val in zip(ax.patches, desa_stat["mean"] ):
    ax.text( bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f"{val/1000000:.1f}", ha = "center", va = "bottom", fontname = "Arial", fontsize = 9, fontweight = "bold")
ax.set_title("Salary According to Department", fontname = "Arial", fontsize = 18, fontweight = "bold")
ax.set_ylabel("Salary (Million VND)", fontname = "Arial", fontsize = 12, fontweight = "bold")
ax.set_xlabel("Department", fontname = "Arial", fontsize = 12, fontweight = "bold")
plt.show()
# Difference between Male and Female Salary

gensa = (cleaned_em.groupby("Gender")["Salary"]
         .agg(["mean","median","std","count"])
         .round(2)
         .sort_values("mean",ascending=False))

print(gensa)

fig, ax = plt.subplots(figsize = (9,6), constrained_layout = True)
sns.barplot( x = gensa.index, y = gensa["mean"], palette="Set2", ax = ax, width = 0.6, edgecolor = "black")
for bar, val in zip(ax.patches, gensa["mean"]):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f"{val/1000000:.2f}",ha="center",va="bottom", fontname = "Arial", fontsize = 9, fontweight = "bold")
ax.set_title("Difference between Male and Female Salary", fontsize = 16, fontname = "Arial", fontweight = "bold")
ax.set_xlabel("Gender",fontname ="Arial", fontsize = 11, fontweight = "bold")
ax.set_ylabel("Salary (Million VND)",fontname ="Arial", fontsize = 11, fontweight = "bold")
plt.show
#Difference between different Education

edusa = (cleaned_em.groupby("Education")["Salary"]
         .agg(["mean", "median", "std", "count"])
         .round(2)
         .sort_values("mean", ascending=False))
print(edusa)

fig, ax = plt.subplots(figsize = (9,6), constrained_layout = True)
sns.barplot(x = edusa.index, y = edusa["mean"], palette="Set3", ax = ax, width = 0.6, edgecolor = "black")
for bar, val in zip(ax.patches, edusa["mean"]):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f"{val/1000000:.2f}",ha = "center", va = "bottom", fontname = "Arial", fontsize = 9, fontweight = "bold")
ax.set_title("Difference between different Education", fontname = "Arial", fontsize = 16, fontweight = "bold")
ax.set_xlabel("Education", fontname = "Arial", fontsize = 16, fontweight = "bold")
ax.set_ylabel("Salary (Million VND)", fontname = "Arial", fontsize = 16, fontweight = "bold")
plt.show
pivot = pd.pivot_table(
    cleaned_em,
    values = "Salary",
    index = "Department",
    columns = "Education",
    aggfunc = "mean",
    fill_value = np.nan
)
pivot = (pivot/1000000).round(2)
print(pivot)

fig, ax = plt.subplots(figsize=(9, 6), constrained_layout=True)
sns.heatmap(pivot, annot = True, fmt = ".0f", cmap = "coolwarm", ax = ax, linewidths=0.5, linecolor="white", annot_kws={"size":9})
ax.set_title("Mean Salary accor (Edu & Department)", fontname= "Arial", fontsize = 16, fontweight = "bold")
ax.set_xlabel("Edu", fontname= "Arial", fontsize = 16)
ax.set_ylabel("Department", fontname= "Arial", fontsize = 16)
plt.show
# Bonus depending on Performance ?

fig, ax = plt.subplots(figsize = (8,5), constrained_layout = True)
sns.scatterplot(x=cleaned_em["Performance"], y = cleaned_em["Bonus_pct"], marker = "o", size = 5, color = "#F5DA27", edgecolor = "black", ax= ax, legend = False)
ax.set_title("Bonus accor Performance",fontname = "Arial", fontsize = 18, fontweight = "bold" )
ax.set_xlabel("Performance (points)",fontname = "Arial", fontsize = 12, fontweight = "bold")
ax.set_ylabel("Bonus (pct)",fontname = "Arial", fontsize = 12, fontweight = "bold")
sns.despine()

plt.show


# Statistical Testing

# Check if Normal Distribution
t, pvalue = stats.shapiro(cleaned_em["Salary"])
print(f"Shapiro Test for Salary : p = {pvalue:.4f}")
if pvalue >= 0.05:
    print("\nData has Normal Distribution (Use T-Test)")
else:
    print("\nData does not have Normal Distribution (Use ManWhitney)")

# Compare Salary between Male and Female
male_sal = cleaned_em.loc[cleaned_em["Gender"]=="Nam", "Salary"]
female_sal = cleaned_em.loc[cleaned_em["Gender"] == "Nữ", "Salary"]

u_stat, mw_p = stats.mannwhitneyu(male_sal, female_sal, alternative="two-sided")
print(f"\nManWhitney Test : p = {mw_p:.4f}")
if mw_p < 0.05 :
    print("Has Difference between Male and Female Salary (Has Statistical Meaning)")
else:
    print("Not enough Statistical Evidence")

# Compare Salary between different Department
group_dept = [group["Salary"].values for name, group in cleaned_em.groupby("Department")]
h_stat , kw_p = stats.kruskal(*group_dept)
print(f"\nKruskal p-value : {kw_p:.4f}")
if kw_p < 0.05:
    print("At least two groups are Different")
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    tukey_dept = pairwise_tukeyhsd(endog=cleaned_em["Salary"], groups=cleaned_em["Department"], alpha= 0.05)
    print(tukey_dept)
else:
    print("No Difference, perhaps random")







































print("\n\n\nIt's not hard, It's just new.")
