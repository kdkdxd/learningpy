
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


# Statistical Testing
# Check if Normal Distribution
t,pvalue1 = stats.shapiro(cleaned_em["Salary"])
print(f"\nShapiro pvalue : {pvalue1:4f}")
if pvalue1 >= 0.05:
    print("Data has Normal Distribution")
else:
    print("Data does not have Normal Distribution")

#Compare Salary between Male and Female
if pvalue1 >= 0.05:
    male_sal = cleaned_em.loc[cleaned_em["Gender"]=="Nam", "Salary"]
    female_sal = cleaned_em.loc[cleaned_em["Gender"]=="Nữ", "Salary"]
    t2,pvalue2 = stats.ttest_ind(male_sal, female_sal)
    print(f"TTest Ind pvalue = {pvalue2:.4f}")
    if pvalue2 < 0.05:
        print("Salary Between Male and Female Salary is Diffent")
    else:
        print("Does not have enough Statistical Evidence")
else:
    male_sal = cleaned_em.loc[cleaned_em["Gender"]=="Nam", "Salary"]
    female_sal = cleaned_em.loc[cleaned_em["Gender"]=="Nữ", "Salary"]
    t3,pvalue3 = stats.mannwhitneyu(male_sal,female_sal)
    print(f"\nManWhitney pvalue : {pvalue3:.4f}")
    if pvalue3 < 0.05:
        print("Salary Between Male and Female Salary is Diffent => Perhaps Different ")
    else:
        print("Does not have enough Statistical Evidence => Perhaps Not Different")

#Compare Salary between Different Department
group_dept = [group["Salary"].values for name, group in cleaned_em.groupby("Department")]
h_stat, kw_p = stats.kruskal(*group_dept)
print(f"\nKruskal pvalue : {kw_p:4f}")
if kw_p < 0.05 :
    print("Data has at least two Department are Different")
else:
    print("No Difference => Perhaps random")




























print("\n\n\nIt's not hard, It's just new.")
