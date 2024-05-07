import pandas as pd
import os
from datetime import datetime

# 定義列名
column_names = ['時間', '里程', '南北向', '車種', '數量']
# 定義列名
column_names2 = ['時間', '里程1', '里程2', '車種', '速度', '數量']

# 初始化兩個空的DataFrame來存儲所有的數據
df_all1 = pd.DataFrame()
df_all2 = pd.DataFrame()

# 遍歷所有可能的小時和分鐘組合
for hour in range(24):
    for minute in range(0, 60, 5):
        # 創建文件名
        filename = f'TDCS_M03A_20240429_{hour:02d}{minute:02d}00.csv'
        # 讀取CSV文件並將其添加到df_all1
        df = pd.read_csv(os.path.join('TDCS_M03A', filename), names=column_names)
        df_all1 = pd.concat([df_all1, df])

        # 創建文件名
        filename = f'TDCS_M05A_20240429_{hour:02d}{minute:02d}00.csv'
        # 讀取CSV文件並將其添加到df_all2
        df = pd.read_csv(os.path.join('TDCS_M05A', filename), names=column_names2)
        df_all2 = pd.concat([df_all2, df])

# 你可以在這裡進行後續的處理

# 修改時間列
df_all1['時間'] = pd.to_datetime(df_all1['時間']).dt.hour * 12 + pd.to_datetime(df_all1['時間']).dt.minute // 5 + 1
# 修改時間列
df_all2['時間'] = pd.to_datetime(df_all2['時間']).dt.hour * 12 + pd.to_datetime(df_all2['時間']).dt.minute // 5 + 1

# 篩選和修改里程列
df_all1['里程'] = df_all1['里程'].apply(lambda x: int(x[3:7]) if x.startswith('01') else None)
# 篩選出開頭為'01'的行，並刪除不符合條件的行
df_all2 = df_all2[df_all2['里程1'].apply(lambda x: str(x).startswith('01'))]
# 篩選和修改里程列DF2
df_all2['里程1'] = df_all2['里程1'].apply(lambda x: int(x[3:7]) if x.startswith('01') else None)
# 篩選出'車種'列中包含數字31的行
df_all2 = df_all2[df_all2['車種'].apply(lambda x: '31' in str(x))]

# 修改南北向列
df_all1['南北向'] = df_all1['南北向'].apply(lambda x: 1 if x == 'N' else (2 if x == 'S' else None))

# 將'車種'和'數量'列的數據轉換為字典，並將字典轉換為DataFrame
df_all1['車種數量'] = df_all1.apply(lambda row: dict(zip(str(row['車種']).split(','), map(int, map(float, str(row['數量']).split(','))))) if pd.notnull(row['車種']) and pd.notnull(row['數量']) else {}, axis=1)
df_all1 = df_all1.drop(columns=['車種', '數量'])
df_all1 = df_all1.join(pd.json_normalize(df_all1['車種數量'])).drop(columns=['車種數量'])

# 合併'時間'，'里程'和'南北向'相同的行，並將相同行的車種數量加總
df_all1 = df_all1.groupby(['時間', '里程', '南北向']).sum().reset_index()

# 更改列名
df_all1.columns = ['時間', '里程', '南北向', '小客車', '小貨車', '大客車', '大貨車', '聯結車']

def match_speed(row):
    matched_row = df_all2[(df_all2['時間'] == row['時間']) & (df_all2['里程1'] == row['里程'])]
    if not matched_row.empty:
        return matched_row.iloc[0]['速度']
    else:
        return None

df_all1['速度'] = df_all1.apply(match_speed, axis=1)

# 保存處理後的DataFrame
df_all1.to_csv('TDCS_M03+05A_feature.csv', index=False)