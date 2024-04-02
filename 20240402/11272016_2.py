import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# 讀取 CSV 文件
weather_data = pd.read_csv('20240402/weather_data.csv')

# 讀取 shape file
taiwan = gpd.read_file('20240402/county/COUNTY_MOI_1090820.shp')

# 繪製台灣地圖
taiwan.plot()
plt.xlim(118,122)
plt.ylim(21,27)


# 在地圖上標出對應的溫度
for i, row in weather_data.iterrows():
    temp = row['Temperature']
    # 獲取縣市的幾何中心點
    city_geom = taiwan.loc[taiwan['COUNTYNAME'] == row['City']].geometry.unary_union.centroid
    # 在繪製文字時使用設定的字體
    plt.text(city_geom.x-0.35, city_geom.y, f'{temp}', fontsize=8)

plt.show()

# 保存到 PNG 文件
plt.savefig('20240402/taiwan_map_tempture.png')