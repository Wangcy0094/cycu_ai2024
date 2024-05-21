import os
import requests
from bs4 import BeautifulSoup
from datetime import timedelta, date

start_date = date(2024, 1, 1)
end_date = date(2024, 4, 30)

# 創建新的資料夾
if not os.path.exists('midexam_practice'):
    os.makedirs('midexam_practice')

current_date = start_date
while current_date <= end_date:
    url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/"
    try:
        response = requests.get(url, timeout=10)  # 設置超時時間為10秒
        soup = BeautifulSoup(response.text, 'html.parser')
        tar_file_found = False
        for link in soup.find_all('a'):
            if f"M05A_{current_date.strftime('%Y%m%d')}.tar.gz" in link.get('href'):
                download_url = url + '/' + link.get('href')
                download_response = requests.get(download_url)
                if download_response.status_code == 200:
                    with open(os.path.join('midexam_practice', f"M05A_{current_date.strftime('%Y%m%d')}.tar.gz"), 'wb') as f:
                        f.write(download_response.content)
                    tar_file_found = True
                    break
        if not tar_file_found:
            # 遍歷每個小時
            for hour in range(24):
                hour_str = str(hour).zfill(2)  # 將小時轉換為兩位數的字符串

                # 遍歷每5分鐘的CSV文件
                for minute in range(0, 60, 5):
                    minute_str = str(minute).zfill(2)  # 將分鐘轉換為兩位數的字符串

                    # 創建文件名
                    filename = f"TDCS_M05A_{current_date.strftime('%Y%m%d')}_{hour_str}{minute_str}00.csv"

                    # 創建完整的URL
                    url = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/{current_date.strftime('%Y%m%d')}/{hour_str}/{filename}"

                    # 下載CSV文件
                    try:
                        download_response = requests.get(url)
                        if download_response.status_code == 200:
                            # 創建每天的資料夾
                            daily_folder = os.path.join('midexam_practice', current_date.strftime('%Y%m%d'))
                            os.makedirs(daily_folder, exist_ok=True)

                            # 將文件保存到每天的資料夾中
                            with open(os.path.join(daily_folder, filename), 'wb') as f:
                                f.write(download_response.content)
                    except requests.exceptions.RequestException as e:
                        print(f"An error occurred when trying to download CSV files: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred when trying to download the tar file: {e}")
    current_date += timedelta(days=1)  # 將當前日期增加一天


# import os
# import requests
# from tqdm import tqdm

# def download_files(base_url, file_prefix):
#     # 創建新的目錄
#     os.makedirs(file_prefix, exist_ok=True)

#     # 遍歷每個小時
#     for hour in range(24):
#         hour_str = str(hour).zfill(2)  # 將小時轉換為兩位數的字符串

#         # 遍歷每5分鐘的CSV文件
#         for minute in range(0, 60, 5):
#             minute_str = str(minute).zfill(2)  # 將分鐘轉換為兩位數的字符串

#             # 創建文件名
#             filename = f"{file_prefix}_20240429_{hour_str}{minute_str}00.csv"

#             # 創建完整的URL
#             url = os.path.join(base_url, hour_str, filename)

#             # 下載CSV文件
#             response = requests.get(url, stream=True)

#             # 檢查請求是否成功
#             if response.status_code == 200:
#                 # 保存文件到新的目錄
#                 with open(os.path.join(file_prefix, filename), 'wb') as f:
#                     for chunk in response.iter_content(chunk_size=1024):
#                         if chunk:
#                             f.write(chunk)
#             else:
#                 print(f"Failed to download {url}")

# # 下載第一個網站的文件
# download_files("https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240429/", "TDCS_M03A")

# # 下載第二個網站的文件
# download_files("https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/", "TDCS_M05A")