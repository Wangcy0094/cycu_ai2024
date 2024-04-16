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