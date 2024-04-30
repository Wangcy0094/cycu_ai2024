import pandas as pd
import os
from datetime import datetime

# 定義列名
column_names = ['時間', '里程', '南北向', '車種', '數量']
# 定義列名
column_names2 = ['時間', '里程1', '里程2', '車種', '速度', '數量']

# 從指定的資料夾中讀取第一個CSV文件，並提供列名
df1 = pd.read_csv(os.path.join('TDCS_M03A', 'TDCS_M03A_20240429_000000.csv'), names=column_names)

# 從指定的資料夾中讀取第二個CSV文件，並提供列名
df2 = pd.read_csv(os.path.join('TDCS_M05A', 'TDCS_M05A_20240429_000000.csv'), names=column_names2)

# 修改時間列
df1['時間'] = pd.to_datetime(df1['時間']).dt.hour * 12 + pd.to_datetime(df1['時間']).dt.minute // 5 + 1

# 篩選和修改里程列
df1['里程'] = df1['里程'].apply(lambda x: int(x[3:7]) if x.startswith('01') else None)
# 篩選出開頭為'01'的行，並刪除不符合條件的行
df2 = df2[df2['里程1'].apply(lambda x: str(x).startswith('01'))]
# 篩選和修改里程列DF2
df2['里程1'] = df2['里程1'].apply(lambda x: int(x[3:7]) if x.startswith('01') else None)
# 篩選出'車種'列中包含數字31的行
df2 = df2[df2['車種'].apply(lambda x: '31' in str(x))]

# 修改南北向列
df1['南北向'] = df1['南北向'].apply(lambda x: 1 if x == 'N' else (2 if x == 'S' else None))

# 將'車種'和'數量'列的數據轉換為字典，並將字典轉換為DataFrame
df1['車種數量'] = df1.apply(lambda row: dict(zip(str(row['車種']).split(','), map(int, map(float, str(row['數量']).split(','))))) if pd.notnull(row['車種']) and pd.notnull(row['數量']) else {}, axis=1)
df1 = df1.drop(columns=['車種', '數量'])
df1 = df1.join(pd.json_normalize(df1['車種數量'])).drop(columns=['車種數量'])

# 合併'時間'，'里程'和'南北向'相同的行，並將相同行的車種數量加總
df1 = df1.groupby(['時間', '里程', '南北向']).sum().reset_index()

# 更改列名
df1.columns = ['時間', '里程', '南北向', '小客車', '小貨車', '大客車', '大貨車', '聯結車']

# 保存處理後的DataFrame
df1.to_csv('TDCS_M03A_20240429_000000_TEST.csv', index=False)

# 顯示df2的資料
df2.to_csv('TDCS_M05A_20240429_000000_TEST.csv', index=False)