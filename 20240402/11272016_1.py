#幫我爬一些網址的資料，使用迴圈搜尋，例如https://www.cwa.gov.tw/rss/forecast/36_01.xml ，這個網址後面的01要形成迴圈，從01~22
#舉例來說分別是https://www.cwa.gov.tw/rss/forecast/36_01.xml ，https://www.cwa.gov.tw/rss/forecast/36_02.xml ，以此類推到https://www.cwa.gov.tw/rss/forecast/36_22.xml
#然後迴圈內要搜尋這個是哪一個縣市名稱，例如在https://www.cwa.gov.tw/rss/forecast/36_01.xml網址中，在它的<description>中最後有個RSS 服務--臺北市，代表臺北市是我要的縣市名稱
#再來第二步要找這個縣市，今日的溫度狀況，例如在網址中有一段title是<![CDATA[ 臺北市04/02 今晚明晨 晴時多雲 溫度: 23 ~ 29 降雨機率: 10% (04/02 17:00發布) ]]>，
#這段文字中有一個溫度: 23 ~ 29，這個就是我要的溫度狀況，而04/02為我要的時間
#最後幫我把這個迴圈列出來的縣市名稱、時間、溫度狀況印出來，要分別對應到正確的縣市名稱、時間、溫度狀況
import requests
import re
import xml.etree.ElementTree as ET
for i in range(1,23):
    url = 'https://www.cwa.gov.tw/rss/forecast/36_{:02d}.xml'.format(i)
    res = requests.get(url)
    root = ET.fromstring(res.text)
    description = root.find('channel/item/description').text
    title = root.find('channel/item/title').text
    city = re.search('RSS 服務--(.+?)，', description).group(1)
    temp = re.search('溫度: (.+?) 降雨機率', title).group(1)
    time = re.search('(\d+/\d+)', title).group(1)
    print(city, time, temp)

#幫我把結果印出來，變成csv檔