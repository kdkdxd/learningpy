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
busy_months = [f"Month:{m}" for m,b in monthly_total.items
               if b>avg]

sorted_spending = dict(sorted(spending.items, key=lambda x : x[1]))
top3 = sorted_spending[:3]

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

labeled = [
    {**t, "label": spending(t["amount"])}
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
for cat,limit in budget.items:
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






















































































































































































































































































































































































































































































































































