import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/"
df = pd.DataFrame()

for i in range(24):
    hour = str(i).zfill(2)  # 將數字轉換為兩位數的字串
    url = base_url + hour + "/"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    for link in soup.find_all("a"):
        if link.get("href").endswith(".csv"):
            csv_url = url + link.get("href")
            df_temp = pd.read_csv(csv_url)
            df = pd.concat([df, df_temp])

df.reset_index(drop=True, inplace=True)