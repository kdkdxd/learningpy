import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


#B1
diem = np.array([4.0, 7.5, 3.5, 8.0, 5.0, 6.5, 2.5, 9.0, 4.5, 7.0])
diem_dat =  diem[diem>=5]
so_dat = len(diem_dat)
so_dat = (diem>5).sum()
tb_dat = diem_dat.mean()

tb_truot = diem[diem<5].mean()

print(so_dat)
print(tb_dat)
print(tb_truot)

#B2
diem = np.array([6,8,7, 5,9,8, 7,6,9, 8,10,9])
print(diem.reshape(4,3))
mean_each_week = np.mean(diem.reshape(4,3), axis =1)
print(mean_each_week)



diem = np.array([6,8,7, 5,9,8, 7,6,9, 8,10,9])
col_mean = np.mean(diem.reshape(4,3), axis =0)
col_std = np.std(diem.reshape(4,3), axis =0)
Z_score = (diem.reshape(4,3) - col_mean)/col_std
print(col_mean)
print(col_std)
print(Z_score)

print("It's not hard, it's just new")





