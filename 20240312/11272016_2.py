import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from datetime import datetime
import os
path = os.path.abspath(__file__)
#get the folder of this file
path = os.path.dirname(path)

# 從 Excel 文件讀取數據
excel_file = '112年1-10月交通事故簡訊通報資料.xlsx'

filepath = os.path.join(path ,excel_file)


# 讀取 Excel 文件
df = pd.read_excel(filepath, sheet_name='交通事故簡報通報資料')
#篩選 欄位名稱 為'國道名稱'與'方向' 的資料， 我只要國道名稱為'國道3號'及方向為'南'及''南向'的資料
df1 = df[(df['國道名稱'] == '國道3號') & (df['方向'].isin(['北', '北向']))]

#把 欄位 '年' '月' '日' '時' '分'
#合併成一個欄位 '日期' , 並且轉換成日期格式
df1['事件開始'] = df1['年'].astype(str) + '-' + df1['月'].astype(str) + '-' + df1['日'].astype(str) + ' ' + df1['時'].astype(str) + ':' + df1['分'].astype(str)
df1['事件開始'] = pd.to_datetime(df1['事件開始'])

#把 欄位 '年' '月' '日' '事件排除'  合併成一個欄位 '事件排除' , 並且轉換成日期格式
df1['事件排除'] = df1['年'].astype(str) + '-' + df1['月'].astype(str) + '-' + df1['日'].astype(str) + ' ' + df1['事件排除'].astype(str)
df1['事件排除'] = pd.to_datetime(df1['事件排除'])

#drop 欄位 '年' '月' '日' '時' '分'
df1 = df1.drop(columns=['年', '月', '日', '時', '分'])


#將 '事件開始' '事件排除' 兩個欄位轉換成 unix time stamp 並使用整數表示
import pandas as pd

# 假設 df 是您的 DataFrame，並且 '事件開始' 和 '事件排除' 是 datetime 欄位

df1['事件開始1'] = df1['事件開始'].apply(lambda x: int(x.timestamp()))
df1['事件排除1'] = df1['事件排除'].apply(lambda x: int(x.timestamp()))

#只印出 '事件開始' '事件排除' '國道名稱' '事件類型' '事件描述'
print(df1[['事件開始', '事件排除', '國道名稱','里程','事件開始1','事件排除1']])

# 設定字體為微軟正黑體
font = FontProperties(fname=r"c:\windows\fonts\msjh.ttc", size=10)

# 假設 df 是您的 DataFrame
for index, row in df1.iterrows():
    plt.plot([row['事件開始1'], row['事件排除1']], [row['里程'], row['里程']])

# 設定字體為支援中文的字體
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  # 這裡使用了系統內建的新細明體，你也可以換成其他支援中文的字體

plt.xlabel('事件時間', fontproperties=font)
plt.ylabel('里程', fontproperties=font)

# 顯示標題為 '國道1號南' 的圖表
plt.title('國道3號北向 學號:11272016', fontproperties=font)

#匯出圖表，檔案名稱為"11272016_國道3號南.png"
plt.savefig('11272016_國道3號北向.png')

plt.show()
