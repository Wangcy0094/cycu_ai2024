import os
import requests
from tqdm import tqdm

def download_files(base_url, file_prefix):
    # 創建新的目錄
    os.makedirs(file_prefix, exist_ok=True)

    # 遍歷每個小時
    for hour in range(24):
        hour_str = str(hour).zfill(2)  # 將小時轉換為兩位數的字符串

        # 遍歷每5分鐘的CSV文件
        for minute in range(0, 60, 5):
            minute_str = str(minute).zfill(2)  # 將分鐘轉換為兩位數的字符串

            # 創建文件名
            filename = f"{file_prefix}_20240429_{hour_str}{minute_str}00.csv"

            # 創建完整的URL
            url = os.path.join(base_url, hour_str, filename)

            # 下載CSV文件
            response = requests.get(url, stream=True)

            # 檢查請求是否成功
            if response.status_code == 200:
                # 保存文件到新的目錄
                with open(os.path.join(file_prefix, filename), 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
            else:
                print(f"Failed to download {url}")

# 下載第一個網站的文件
download_files("https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240429/", "TDCS_M03A")

# 下載第二個網站的文件
download_files("https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/", "TDCS_M05A")