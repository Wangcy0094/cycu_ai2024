import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/"

filename = "TDCS_M04A_20240325_000000.csv"

#filename 最後面的數字代表的是小時 分鐘 秒 ，例如000000代表00:00:00
#000500代表00:05:00 以此類推
#如果每5分鐘一筆資料，那麼一小時會有12筆資料
#利用迴圈產生檔名清單
#例如 TDCS_M04A_20240325_000000.csv , TDCS_M04A_20240325_000500.csv
for i in range(0, 24):
    for j in range(0, 60, 5):
        filename = "TDCS_M04A_20240325_" + str(i).zfill(2) + str(j).zfill(2) + "00.csv"
        print(filename)
        url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/" + str(i).zfill(2) + "/"
        url += filename
        print(url)
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
            f.close()
        print("Save", filename)