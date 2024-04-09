import pandas as pd

# 讀取CSV文件
df = pd.read_csv('earthquake.csv', encoding='big5', skiprows=1)

#確認有哪些columns
#print(df.columns)

# 選取需要的列
df = df[['地震時間', '經度', '緯度', '規模']]

# 將地震時間轉換為datetime對象
df['地震時間'] = pd.to_datetime(df['地震時間'])

# 選取2024/4/3 07:58:09 AM到2024/4/9的數據
start_date = pd.to_datetime('2024/4/3 07:58:09 AM')
end_date = pd.to_datetime('2024/4/10')
df = df[(df['地震時間'] >= start_date) & (df['地震時間'] < end_date)]

df.to_csv('filtered_data.csv', index=False)