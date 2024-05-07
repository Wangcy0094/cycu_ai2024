import pandas as pd
import os
from datetime import datetime

# 定義列名
column_names2 = ['時間', '里程1', '里程2', '車種', '速度', '數量']

# 創建一個空的DataFrame
df_all = pd.DataFrame(columns=column_names2)

# 創建一個迴圈來生成所有可能的時間組合
for hour in range(24):
    for minute in range(0, 60, 5):
        # 使用時間組合來生成文件名
        filename = f'TDCS_M05A_20240429_{hour:02d}{minute:02d}00.csv'
        # 讀取文件
        df2 = pd.read_csv(os.path.join('TDCS_M05A', filename), names=column_names2)
        # 修改時間列
        df2['時間'] = pd.to_datetime(df2['時間']).dt.hour * 12 + pd.to_datetime(df2['時間']).dt.minute // 5 + 1
        # 篩選出開頭為'01'的行，並刪除不符合條件的行
        df2 = df2[df2['里程1'].apply(lambda x: str(x).startswith('01'))]
        # 篩選和修改里程列DF2
        df2['里程1'] = df2['里程1'].apply(lambda x: int(x[3:7]) if x.startswith('01') else None)
        # 篩選和修改里程列DF2
        df2['里程2'] = df2['里程2'].apply(lambda x: int(x[3:7]) if x.startswith('01') else None)
        # 篩選出'車種'列中包含數字31的行
        df2 = df2[df2['車種'].apply(lambda x: '31' in str(x))]
        # 將讀取的數據添加到df_all中
        df_all = pd.concat([df_all, df2]) 

# 顯示df_all的資料
df_all.to_csv('TDCS_M05A.csv', index=False)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
df_all['顏色'] = df_all['速度'].apply(speed_to_color)

# 創建3D圖形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 繪製散點圖
scatter = ax.scatter(df_all['時間'], df_all['里程1'], df_all['數量'], c=df_all['顏色'], marker='.', s=1)

# 設置標籤
ax.set_xlabel('time')
ax.set_ylabel('place')
ax.set_zlabel('number')

#匯出圖形
plt.savefig('TDCS_M05A.png')