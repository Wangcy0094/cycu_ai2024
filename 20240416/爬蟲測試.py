import requests
from bs4 import BeautifulSoup
import pandas as pd

# 地震詳情頁面的URLs
urls = [
    'https://scweb.cwa.gov.tw/zh-tw/earthquake/details/2024040307580972019',
    'https://scweb.cwa.gov.tw/zh-tw/earthquake/details/2024041304002940199'
]

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
        details = soup.find_all('div', class_='text')
        time = details[0].text.strip()
        location = details[1].text.strip().split(' ')
        longitude = location[1]
        latitude = location[3]
        magnitude = details[3].text.strip()

        # 將資訊添加到DataFrame
        df = df.append({'地震時間': time, '經度': longitude, '緯度': latitude, '規模': magnitude}, ignore_index=True)
    else:
        print(f"無法訪問 {url}")

# 輸出DataFrame
print(df)