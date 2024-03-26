import pandas as pd
import os

# 定義資料夾路徑
folder_path = './'

# 儲存所有 DataFrame 的列表
dfs = []

# 迴圈讀取每個 CSV 檔案
for hour in range(0, 24):
    for minute in range(0, 60, 5):
        # 建立檔案名稱
        filename = f"TDCS_M04A_20240325_{hour:02d}{minute:02d}00.csv"
        
        # 讀取 CSV 檔案轉換為 DataFrame
        df = pd.read_csv(os.path.join(folder_path, filename))
        
        # 如果這是第一個 DataFrame，則儲存其欄位名稱
        if hour == 0 and minute == 0:
            columns = df.columns
        else:
            # 將 DataFrame 的欄位名稱設定為第一個 DataFrame 的欄位名稱
            df.columns = columns
        
        # 將 DataFrame 加到列表中
        dfs.append(df)

        # 如果時間超過 23:55，則跳出迴圈
        if hour == 23 and minute == 55:
            break

# 將所有的 DataFrame 合併為一個
result = pd.concat(dfs, ignore_index=True)

# 匯出為一個 CSV 檔案
result.to_csv(os.path.join(folder_path, '288筆資料合併結果.csv'), index=False)