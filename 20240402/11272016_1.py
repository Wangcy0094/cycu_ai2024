#幫我爬一些網址的資料，使用迴圈搜尋，例如https://www.cwa.gov.tw/rss/forecast/36_01.xml ，這個網址後面的01要形成迴圈，從01~22
#舉例來說分別是https://www.cwa.gov.tw/rss/forecast/36_01.xml ，https://www.cwa.gov.tw/rss/forecast/36_02.xml ，以此類推到https://www.cwa.gov.tw/rss/forecast/36_22.xml
#然後迴圈內要搜尋這個是哪一個縣市名稱，例如在https://www.cwa.gov.tw/rss/forecast/36_01.xml網址中，在它的<description>中最後有個RSS 服務--臺北市，代表臺北市是我要的縣市名稱
#再來第二步要找這個縣市，今日的溫度狀況，例如在網址中有一段title是<![CDATA[ 臺北市04/02 今晚明晨 晴時多雲 溫度: 23 ~ 29 降雨機率: 10% (04/02 17:00發布) ]]>，
#這段文字中有一個溫度: 23 ~ 29，這個就是我要的溫度狀況，而04/02為我要的時間
#最後幫我把這個迴圈列出來的縣市名稱、時間、溫度狀況印出來，要分別對應到正確的縣市名稱、時間、溫度狀況
# crawler from rss of central weather agency
import re
import requests
import xml.etree.ElementTree as ET
import json
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import os

import feedparser

# url = https://www.cwa.gov.tw/rss/forecast/36_01.xml
# 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, to 22

data = []

for num in range(1, 23):
    url = 'https://www.cwa.gov.tw/rss/forecast/36_' + str(num).zfill(2) + '.xml'
    response = requests.get(url)
    feed = feedparser.parse(response.content)

    for entry in feed.entries:
        # 如果 entry.title 包含 "一週天氣預報"，則跳過這個 entry
        if "一週天氣預報" in entry.title:
            continue

        city_match = re.search('^(.+?)\d', entry.title)
        date_match = re.search('(\d+/\d+)', entry.title)
        temp_match = re.search('溫度: (.+?) 降雨機率:', entry.title)

        if city_match:
            city = city_match.group(1)
        else:
            city = "未知城市"

        if date_match:
            date = date_match.group(1)
        else:
            date = "未知日期"

        if temp_match:
            temp = temp_match.group(1)
        else:
            temp = "未知溫度"

        data.append([city, date, temp])
        print(city, date, temp)
    
    print("=======================================")
# 將結果存入 DataFrame
df = pd.DataFrame(data, columns=['City', 'Date', 'Temperature'])

# 將 DataFrame 輸出成 CSV 文件
df.to_csv('20240402/weather_data.csv', index=False)
