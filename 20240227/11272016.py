print("Hello World!")

#https://news.pts.org.tw/xml/newsfeed.xml

# 引入requests模組，用於發送HTTP請求
import requests
# 引入BeautifulSoup模組，用於解析HTML或XML文件
from bs4 import BeautifulSoup

# 定義要爬取的網頁URL
url = 'https://news.pts.org.tw/xml/newsfeed.xml'
# 使用requests.get方法發送GET請求到指定的URL，並將回應存入response變數
response = requests.get(url)
# 使用BeautifulSoup解析response的內容，並指定解析器為'lxml-xml'
soup = BeautifulSoup(response.content, 'lxml-xml')

# 使用BeautifulSoup的find_all方法找出所有的'title'標籤，並將結果存入titles變數
titles = soup.find_all('title')

# 迴圈遍歷titles，對每一個title，打印其文字內容
for title in titles:
    print(title.text)
    #印出 summary
    print(title.find_next('summary').text)
    #幫我確認以上列出的新聞標題有沒有YouBike的字串 有的話幫我寫一個excel的檔案
    if 'YouBike' in title.text:
        print('有YouBike')
        #寫一個excel的檔案
        import openpyxl
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet['A1'] = title.text
        sheet['B1'] = title.find_next('summary').text
        wb.save('news.xlsx')
    else:
        print('沒有YouBike')


    print('---------------------------------------------')
