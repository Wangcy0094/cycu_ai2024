#我要讀取midexam_practice資料夾內的檔案，底下還會有個20240429的資料夾，裡面會有很多csv檔案，我要讀取這些csv檔案，
#並且將這些檔案的內容合併成一個檔案，並且將這個檔案命名為20240429_M05Amerge.csv，最後將這個檔案放到midexam_practice資料夾底下

import os
import csv
import pandas as pd

# 創建一個空的列表來存儲所有的行
all_rows = []

# 遍歷midexam_practice資料夾，讀取20240429資料夾中的所有CSV文件
for root, dirs, files in os.walk(os.path.join('midexam_practice', '20240429')):
    for file in files:
        if file.endswith('.csv'):
            with open(os.path.join(root, file), 'r', newline='', encoding='utf-8-sig') as f:
                reader = csv.reader(f)
                # 跳過標題行
                next(reader)
                # 遍歷每一行
                for row in reader:
                    all_rows.append(row)

#篩選第四欄是"31"的行，第四欄不是"31"的行不要
all_rows = [row for row in all_rows if row[3] == '31']

# 將所有行轉換為 DataFrame
df = pd.DataFrame(all_rows, columns=['TimeInterval', 'GantryFrom', 'GantryTo', 'VehicleType', 'SpaceMeanSpeed', 'Traffic'])
print(df)

#接著做一個動態地圖，將所有的車輛類型為31的車輛的平均速度繪製在地圖上，並且將這個地圖命名為20240429_M05A31.html，最後將這個地圖放到midexam_practice資料夾底下
import folium

# 創建一個地圖對象
m = folium.Map(location=[25.033903, 121.564509], zoom_start=12)

# 繪製所有車輛類型為31的車輛的平均速度
for index, row in df.iterrows():
    if row['VehicleType'] == '31':
        folium.Marker([float(row['GantryFrom'].split('K')[1]), float(row['GantryFrom'].split('K')[0])], popup=f"Space Mean Speed: {row['SpaceMeanSpeed']}").add_to(m)

# 將地圖保存為一個HTML文件
m.save(os.path.join('midexam_practice', '20240429_M05A31.html'))