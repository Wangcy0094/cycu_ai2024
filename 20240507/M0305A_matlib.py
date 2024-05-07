import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
from datetime import datetime


# 讀取CSV文件
df = pd.read_csv('TDCS_M03+05A_feature.csv')

# 定義速度顏色對應函數
def speed_to_color(speed):
    if speed > 80:
        return 'green'
    elif 60 <= speed <= 80:
        return 'yellow'
    elif 40 <= speed < 60:
        return 'orange'
    elif 20 <= speed < 40:
        return 'red'
    else:
        return 'purple'

# 將速度轉換為顏色
df['顏色'] = df['速度'].apply(speed_to_color)

#根據"方向"列的值將數據分為兩個子集
df_north = df[df['南北向'] == 1]
df_south = df[df['南北向'] == 2]

# 創建3D圖形
fig_north = plt.figure()
ax_north = fig_north.add_subplot(111, projection='3d')
fig_south = plt.figure()
ax_south = fig_south.add_subplot(111, projection='3d')

# 繪製散點圖，設置marker為'o'以獲得圓點
ax_north.scatter(df_north['時間'], df_north['里程'], df_north['小客車'], c=df_north['顏色'], alpha=0.5, marker='.', s=1)
ax_south.scatter(df_south['時間'], df_south['里程'], df_south['小客車'], c=df_south['顏色'], alpha=0.5, marker='.', s=1)

# 設定X、Y和Z軸的標籤
ax_north.set_xlabel('time')
ax_north.set_ylabel('place')
ax_north.set_zlabel('number')
ax_south.set_xlabel('time')
ax_south.set_ylabel('place')
ax_south.set_zlabel('number')

# 匯出圖片
fig_north.savefig('M0305A_north_speed.png')
fig_south.savefig('M0305A_south_speed.png')