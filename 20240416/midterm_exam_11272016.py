from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# 建立一個新的 Chrome 瀏覽器實例
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": os.getcwd(),  # 下載路徑設為當前工作目錄
    "download.prompt_for_download": False,  # 禁用下載確認對話框
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})

driver = webdriver.Chrome(options=chrome_options)

# 讓瀏覽器打開指定的 URL
driver.get('https://scweb.cwa.gov.tw/zh-tw/earthquake/data/')

# 等待網頁加載完成
wait = WebDriverWait(driver, 10)
csv_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[title="匯出地震資料 (地震活動彙整.csv)"]')))

# 點擊 CSV 下載連結
csv_link.click()

# 等待下載完成
import time
time.sleep(5)  # 等待 5 秒讓下載完成

# 關閉瀏覽器
driver.quit()

import shutil
# 找到下載的檔案名稱
downloaded_file = max([os.getcwd() + "\\" + f for f in os.listdir(os.getcwd())], key=os.path.getctime)

# 重新命名下載的檔案
shutil.move(downloaded_file, os.getcwd() + "\\earthquake.csv")
print('---------------------------------')
import pandas as pd

# 讀取CSV檔案，指定編碼為'big5'，並跳過第一行，只讀取指定的欄位
df = pd.read_csv('earthquake.csv', encoding='big5', skiprows=1, usecols=['地震時間', '經度', '緯度', '規模'])

# 將"地震時間"列轉換為datetime對象
df['地震時間'] = pd.to_datetime(df['地震時間'])

# 過濾出2024/4/3 07:58:09 AM到2024/4/10之前的資料
start_date = pd.to_datetime('2024/4/3 07:58:09 AM')
end_date = pd.to_datetime('2024/4/10')
filtered_df = df[(df['地震時間'] >= start_date) & (df['地震時間'] < end_date)]

# 顯示過濾後的資料
print(filtered_df)

print('---------------------------------')

import folium
from folium.plugins import TimestampedGeoJson

# 創建一個以台灣為中心的地圖
m = folium.Map(location=[23.8, 120.9])

# 創建一個空的GeoJson列表
data = []

# 遍歷DataFrame中的每一行
for index, row in filtered_df.iterrows():
    # 為每個地震創建一個GeoJson點
    data.append({
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [row['經度'], row['緯度']],
        },
        'properties': {
            'time': row['地震時間'].isoformat(),  # 使用地震的時間
            'popup': f"時間: {row['地震時間']}, 經度: {row['經度']}, 緯度: {row['緯度']}, 規模: {row['規模']}",  # 在popup中顯示地震的資訊
            'icon': 'circle',
            'iconstyle': {
                'fillColor': 'red',
                'fillOpacity': 0.6,
                'stroke': 'false',
                'radius': 5
            }
        }
    })

# 將GeoJson列表添加到地圖上
TimestampedGeoJson(
    {'type': 'FeatureCollection', 'features': data},
    period='PT1H',
    add_last_point=True,
).add_to(m)

# 將地圖保存為HTML檔案
m.save('earthquake_map_11272016.html')