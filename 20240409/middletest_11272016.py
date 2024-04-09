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
#繪製台灣地圖
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 讀取 shape file
taiwan = gpd.read_file('20240402/county/COUNTY_MOI_1090820.shp')
plt.xlim(118,122)
plt.ylim(21,27)

#在地圖上標出地震的位置
for i, row in df.iterrows():
    # 獲取地震的經緯度
    lon, lat = row['經度'], row['緯度']
    # 在地圖上標出地震的位置
    plt.scatter(lon, lat, color='red', s=row['規模']*10)
    plt.text(lon, lat, f'{row["規模"]}', fontsize=8)

# 設定 x 軸、y 軸的標籤和圖表的標題
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.title('11272016 Chen-Yu,Wang')

plt.show()

# 保存到 PNG 文件
plt.savefig('earthquake_map.png')