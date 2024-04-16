import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

# # 起始日期和結束日期
# start_date = datetime(2024, 4, 3)
# end_date = datetime(2024, 4, 4)

# # 規模和編號的範圍
# magnitude_range = range(0, 100)  # 假設規模的範圍是 0 到 99
# id_range = range(0, 1000)  # 假設編號的範圍是 0 到 999

# # 生成所有的 URL
# urls = []
# date = start_date
# while date <= end_date:
#     for hour in range(24):
#         for minute in range(60):
#             for second in range(60):
#                 for magnitude in magnitude_range:
#                     for id in id_range:
#                         # 生成 URL
#                         url = f"https://scweb.cwa.gov.tw/zh-tw/earthquake/details/{date.strftime('%Y%m%d%H%M%S')}{magnitude:02d}{id:03d}"
#                         urls.append(url)
#     date += timedelta(days=1)

# 創建一個空的DataFrame
df = pd.DataFrame(columns=['地震時間', '經度', '緯度', '規模'])

for url in urls:
    # 發送GET請求
    response = requests.get(url)

    # 檢查請求是否成功
    if response.status_code == 200:
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取發震時間、震央位置和芮氏規模
        # 提取發震時間、震央位置和芮氏規模
        details = soup.find_all('div', class_='text')
        # 提取並轉換時間
        time = details[0].text.strip()
        time = time.replace('年', '/').replace('月', '/').replace('日', '').replace('時', ':').replace('分', ':').replace('秒', '')
        date, time_part = time.split(' ')
        year, month, day = date.split('/')
        year = str(int(year) + 1911)  # 將民國年份轉換為西元年份
        hour, minute, second = time_part.split(':')
        hour = hour.zfill(2)  # 如果小時是一位數，則在前面添加一個 '0'
        minute = minute.zfill(2)  # 如果分鐘是一位數，則在前面添加一個 '0'
        second = second.zfill(2)  # 如果秒數是一位數，則在前面添加一個 '0'
        time = f'{year}/{month}/{day} {hour}:{minute}:{second}'
        time = datetime.strptime(time, '%Y/%m/%d %H:%M:%S')  # 將字符串轉換為 datetime 物件
        time = time.strftime('%Y/%m/%d %I:%M:%S %p')  # 將 datetime 物件轉換為指定的格式
        location = details[1].text.strip().split(' ')
        latitude = location[1].split('°')[0]  # 北緯後面的數字
        longitude = location[4].split('°')[0]  # 東經後面的數字
        magnitude = details[3].text.strip()

        # 將資訊添加到DataFrame
        new_row = pd.DataFrame([{'地震時間': time, '經度': longitude, '緯度': latitude, '規模': magnitude}])
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        print(f"無法訪問 {url}")

# 輸出DataFrame
print(df)

#輸出為CSV檔案，編碼為'big5'
df.to_csv('earthquake.csv', encoding='big5', index=False)