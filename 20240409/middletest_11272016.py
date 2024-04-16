import pandas as pd

# 讀取CSV文件
df = pd.read_csv('earthquake.csv', encoding='big5', skiprows=1)

#確認有哪些columns
#print(df.columns)

# 選取需要的列
df = df[['地震時間', '經度', '緯度', '規模']]

# 將地震時間轉換為datetime對象
df['地震時間'] = pd.to_datetime(df['地震時間'])

# 選取2024/4/3 07:58:09 AM到2024/4/9的數據
start_date = pd.to_datetime('2024/4/3 07:58:09 AM')
end_date = pd.to_datetime('2024/4/10')
df = df[(df['地震時間'] >= start_date) & (df['地震時間'] < end_date)]

df.to_csv('filtered_data.csv', index=False)

print('---------------------------------')
import folium
import matplotlib.colors as mcolors

# 創建一個以台灣為中心的地圖
m = folium.Map(location=[23.8, 121], zoom_start=7)

# 創建一個顏色映射
cmap = mcolors.LinearSegmentedColormap.from_list("", ['lightblue', 'deepskyblue', 'yellow', 'orange', 'red'])
norm = mcolors.Normalize(vmin=df['規模'].min(), vmax=df['規模'].max())

# 在地圖上標出地震的位置
for i, row in df.iterrows():
    # 獲取地震的經緯度
    lon, lat = row['經度'], row['緯度']
    # 創建一個彈出窗口，顯示地震的時間、經度、緯度和規模
    popup = folium.Popup(f"時間: {row['地震時間']}<br>經度: {lon}<br>緯度: {lat}<br>規模: {row['規模']}", max_width=200)
    # 在地圖上標出地震的位置，並添加彈出窗口
    folium.CircleMarker(
        location=[lat, lon],
        radius=row['規模']*2,  # 設定圓點的大小
        color=mcolors.to_hex(cmap(norm(row['規模']))),  # 根據規模選擇顏色
        fill=True,
        fill_color=mcolors.to_hex(cmap(norm(row['規模']))),  # 根據規模選擇顏色
        popup=popup  # 添加彈出窗口
    ).add_to(m)

# 保存地圖到 HTML 文件
m.save('earthquake_map.html')

print('---------------------------------')
from ipyleaflet import Map, Marker, basemaps
from folium.plugins import TimestampedGeoJson
from datetime import datetime, timedelta
import json

# 創建一個以台灣為中心的地圖
m = folium.Map(location=[23.8, 121], zoom_start=7)

# 指定開始時間
start_time = datetime.strptime('2024/4/3 7:58', '%Y/%m/%d %H:%M')

# 創建一個TimestampedGeoJson對象
timestamped_geojson = TimestampedGeoJson(
    {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [row['經度'], row['緯度']],
                },
                "properties": {
                    "times": [(start_time + timedelta(days=i)).isoformat(), (start_time + timedelta(days=i+1)).isoformat()],
                    "style": {"color": mcolors.to_hex(cmap(norm(row['規模'])))},
                    "icon": "circle",
                },
            } for i, row in df.iterrows()
        ],
    },
    period="PT1H",
    add_last_point=True,
    auto_play=False,
    loop=False,
    max_speed=1,
    loop_button=True,
    date_options='YYYY/MM/DD',
    time_slider_drag_update=True,
)

m.add_child(timestamped_geojson)

# 保存地圖到 HTML 文件
m.save('earthquake_map2.html')