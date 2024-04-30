import requests
import os
from datetime import datetime, timedelta

# 起始和結束日期
start_date = datetime(2024, 4, 16)
end_date = datetime(2024, 4, 23)

# 當前日期
current_date = start_date

while current_date <= end_date:
    # 創建新的資料夾
    os.makedirs(f"Data_{current_date.strftime('%Y%m%d')}", exist_ok=True)

    for hour in range(24):
        for minute in range(0, 60, 5):
            # 生成目標網址
            url = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/{current_date.strftime('%Y%m%d')}/{str(hour).zfill(2)}/TDCS_M04A_{current_date.strftime('%Y%m%d')}_{str(hour).zfill(2)}{str(minute).zfill(2)}00.csv"

            # 下載檔案並寫入到新的資料夾中
            with open(f"Data_{current_date.strftime('%Y%m%d')}/TDCS_M04A_{current_date.strftime('%Y%m%d')}_{str(hour).zfill(2)}{str(minute).zfill(2)}00.csv", 'wb') as f:
                f.write(requests.get(url).content)

    # 將當前日期加一天
    current_date += timedelta(days=1)