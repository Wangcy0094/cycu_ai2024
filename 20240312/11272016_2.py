import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from datetime import datetime

# 讀取 csv 檔案
df = pd.read_csv('112年1-10月交通事故簡訊通報資料.csv')

# 先幫我把欄位"年""月""日""時""分"合併成一個欄位"開始時間"，並轉換成datetime格式
df['開始時間'] = df['年'].astype(str) + '-' + df['月'].astype(str) + '-' + df['日'].astype(str) + ' ' + df['時'].astype(str) + ':' + df['分'].astype(str)

# 再幫我把欄位"事件排除"與同一列的"年""月""日"合併成一個欄位"結束時間"，並轉換成datetime格式
df['結束時間'] = df['年'].astype(str) + '-' + df['月'].astype(str) + '-' + df['日'].astype(str) + ' ' + df['事件排除'].astype(str)

#drop 欄位 "年""月""日""時""分"
df = df.drop(columns=['年', '月', '日', '時', '分'])

# 轉換時間欄位為 datetime 類型，並用整數表示
df['開始時間'] = pd.to_datetime(df['開始時間']).astype(int)
df['結束時間'] = pd.to_datetime(df['結束時間']).astype(int)

# 設定字體為微軟正黑體
font = FontProperties(fname=r"c:\windows\fonts\msjh.ttc", size=10)

# 繪製圖表
plt.figure(figsize=(10, 6))

for index, row in df.iterrows():
    plt.plot([row['開始時間'], row['結束時間']], [row['里程'], row['里程']], color='blue')

# 設定 x 軸和 y 軸的標籤
plt.xlabel('時間', fontproperties=font)
plt.ylabel('里程', fontproperties=font)

# 顯示圖表
plt.show()
