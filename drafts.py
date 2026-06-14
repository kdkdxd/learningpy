import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np




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
sns.set_theme(style="whitegrid")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(data=dfsea, x = "Luong", bins = 25, color = "blue", kde = "True", ax=ax)
sns.kdeplot(data=dfsea, x="Luong", bw_adjust=0.5)
ax.set_title("Phân phối lương", fontname="Arial", fontsize=25, fontweight="bold")
ax.set_xlabel("Lương(Triệu Đồng)", fontname="Arial", fontsize=15)
ax.set_ylabel("Số nhân viên", fontname="Arial", fontsize=15)
ax.set_ylim(0,14)

plt.tight_layout()
























plt.show()































print("It's not hard, it's just new.")