import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

print("It's not hard, it's just new.")

diem = np.array([4.5, 6.0, 7.5, 8.0, 9.5, 5.0, 7.0])
normalize = (diem-diem.min()) / (diem.max()-diem.min())
print(normalize)

nhiet_do = np.array([28.0, 72.0, 31.5, -5.0, 29.0, 41.0, 25.5])
nhiet_do[(nhiet_do<10)|(nhiet_do>40)] = np.nan
print(nhiet_do)


gia_tri = np.array([1, 2, 3, 4, 5])
matrix = np.diag(gia_tri)
print(matrix)


diem = np.array([[0,0], [1,0], [0,1], [1,1]], dtype=float)
diff  = diem[:, np.newaxis, :] - diem[np.newaxis, :, :]
ds_matrix = np.sqrt((diff**2).sum(axis=2))
print(ds_matrix.round(3))







