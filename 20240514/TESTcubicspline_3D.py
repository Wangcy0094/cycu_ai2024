import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import matplotlib.colors as mcolors
import matplotlib.cm as cm

# 讀取CSV文件，使用'big5'編碼
df = pd.read_csv('TDCS_M0305A_20240429_all.csv', encoding='big5')

# 對時間和里程數據進行網格化
# 假設 x (時間) 和 y (里程) 已經是規則的網格數據
x = np.linspace(df['時間'].min(), df['時間'].max(), num=1000) # 調整 num 以匹配數據點的密度
y = np.linspace(df['地點'].min(), df['地點'].max(), num=1000)
x, y = np.meshgrid(x, y)

# 插值找到每個 (x, y) 點對應的 z (車流量)
z = griddata((df['時間'], df['地點']), df['小客車'], (x, y), method='linear')
speed = griddata((df['時間'], df['地點']), df['小客車旅行速度'], (x, y), method='linear')

# 創建一個自定義的顏色映射
cmap = mcolors.ListedColormap(['purple', 'yellow', 'orange', 'yellow', 'green'])
norm = mcolors.BoundaryNorm([0, 20, 40, 60, 80, np.inf], cmap.N)

# 創建一個 ScalarMappable 對象
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(221, projection='3d')
# 繪製曲面圖
surf = ax1.plot_surface(x, y, z, facecolors=sm.to_rgba(speed))

# 設置坐標軸標籤
ax1.set_xlabel('Time')
ax1.set_ylabel('Mileage')
ax1.set_zlabel('Traffic Volume')
ax1.view_init(elev=30, azim=45)

ax2 = fig.add_subplot(222, projection='3d')
# 繪製曲面圖
surf = ax2.plot_surface(x, y, z, facecolors=sm.to_rgba(speed))
# 設置坐標軸標籤
ax2.set_xlabel('Time')
ax2.set_ylabel('Mileage')
ax2.set_zlabel('Traffic Volume')
ax2.view_init(elev=30, azim=135)

ax3 = fig.add_subplot(223, projection='3d')
# 繪製曲面圖
surf = ax3.plot_surface(x, y, z, facecolors=sm.to_rgba(speed))
# 設置坐標軸標籤
ax3.set_xlabel('Time')
ax3.set_ylabel('Mileage')
ax3.set_zlabel('Traffic Volume')
ax3.view_init(elev=30, azim=225)

ax4 = fig.add_subplot(224, projection='3d')
# 繪製曲面圖
surf = ax4.plot_surface(x, y, z, facecolors=sm.to_rgba(speed))
# 設置坐標軸標籤
ax4.set_xlabel('Time')
ax4.set_ylabel('Mileage')
ax4.set_zlabel('Traffic Volume')
ax4.view_init(elev=30, azim=315)

plt.suptitle('11272016')
plt.tight_layout()
# 顯示圖形
plt.savefig('M0305A_cubicspline_3D.png')