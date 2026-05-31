import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


np.random.seed(42)
df = pd.DataFrame({
    "OrderCode": range(1001),
    "Price": np.random.exponential(500000, 1001).round(),
    "Area":np.random.choice(["HCM","NY","BK","JK"], 1001, p = [0.4,0.35,0.15,0.1])
})
ex200 = df.sample(n=200, random_state=42)
ex15pct = df.sample(frac=0.25, random_state=42)

ex_stratified =df.groupby("Area", group_keys=False).sample(
    frac=0.25,
    random_state=42
)

print(f"Example 200:{ex200}")
print(f"Example 15%:{ex15pct}")
print(f"Example Stratified:{ex_stratified["Area"].value_counts()}")



























































































































































print("It's not hard, it's just new.")