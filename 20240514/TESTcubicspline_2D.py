import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import pandas as pd

# 讀取CSV文件，使用'big5'編碼
df = pd.read_csv('TDCS_M0305A_20240429_all.csv', encoding='big5')

# 選擇下午6點的時間
df_six_pm = df[df['時間'] == 217]

# 將數據分為兩個子集
df_north = df_six_pm[df_six_pm['方向'] == 1]
df_south = df_six_pm[df_six_pm['方向'] == 2]

# 為北向數據創建CubicSpline對象
x_north = df_north['地點']
y_north = df_north['小客車']
cs_north = CubicSpline(x_north, y_north)

# 為南向數據創建CubicSpline對象
x_south = df_south['地點']
y_south = df_south['小客車']
cs_south = CubicSpline(x_south, y_south)

# 創建新的x值範圍
xs_north = np.linspace(min(x_north), max(x_north), 1000)
xs_south = np.linspace(min(x_south), max(x_south), 1000)

# 計算對應的y值
ys_north = cs_north(xs_north)
ys_south = cs_south(xs_south)

# 繪製結果
plt.figure(figsize=(10, 6))
plt.plot(x_north, y_north, 'o', label='Northbound Original Data')
plt.plot(xs_north, ys_north, label="Northbound Cubic Spline Fitted Curve")
plt.plot(x_south, y_south, 'o', label='Southbound Original Data')
plt.plot(xs_south, ys_south, label="Southbound Cubic Spline Fitted Curve")
plt.xlabel('Mileage')
plt.ylabel('Traffic Volume')
plt.title('6 PM Traffic Volume')
plt.legend(loc='best')
plt.show()

# 匯出圖片
plt.savefig('M0305A_6pm_cubicspline.png')