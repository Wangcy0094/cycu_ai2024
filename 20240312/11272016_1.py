import pandas as pd

# 讀取 csv 檔案
df = pd.read_csv('112年1-10月交通事故簡訊通報資料.csv')

# 過濾出國道名稱為 "國道1號" 且方向為 "南" 或 "南向" 的資料
filtered_df = df[(df['國道名稱'] == '國道1號') & (df['方向'].isin(['南', '南向']))]

# 計算每個里程的事故次數
result = filtered_df.groupby('里程')['里程'].count()

# 將結果轉換為 DataFrame
result_df = pd.DataFrame(result)

# 重新命名欄位
result_df.columns = ['發生次數']

# 重設索引
result_df = result_df.reset_index()

# 顯示結果
print(result_df)

#顯示發生次數最多的里程
max_mileage = result_df[result_df['發生次數'] == result_df['發生次數'].max()]
print('發生次數最多的里程:', max_mileage)


# 將結果繪製成圖表
result_df.plot(kind='bar', x='里程', y='發生次數')


# 顯示圖表
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 設定字體為微軟正黑體
font = FontProperties(fname=r"c:\windows\fonts\msjh.ttc", size=10)

# 設定 legend 的字體
plt.legend(prop=font)

# 計算每隔多少個里程數顯示一個標籤
step = len(result_df['里程']) // 10

# 顯示 x 軸標籤
plt.xticks(range(0, len(result_df['里程']), step), result_df['里程'][::step], rotation=90, fontproperties=font)

# 顯示 y 軸標籤並顯示名稱
plt.ylabel('發生次數', fontproperties=font)
plt.xlabel('里程', fontproperties=font)
plt.title('國道1號南向交通事故發生次數', fontproperties=font)

# 顯示圖表
plt.show()


# 將結果寫入 csv 檔案
result_df.to_csv('國道1號南向交通事故發生次數.csv', index=False)