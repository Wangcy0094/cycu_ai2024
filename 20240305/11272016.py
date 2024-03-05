import requests
from bs4 import BeautifulSoup
import pandas as pd

# 獲取網頁內容
response = requests.get('https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx')

# 解析網頁內容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的 table 標籤
tables = soup.find_all('table')

# 將找到的 table 標籤轉換為 DataFrame
df1 = pd.read_html(str(tables[0]))[0]
df2 = pd.read_html(str(tables[1]))[0]

print(df1)
print(df2)

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 使用支援中文的字體
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  # 路徑請換成你的系統中的實際字體路徑

# 刪除缺失值
df2 = df2.dropna(subset=['無鉛汽油92', '無鉛汽油95', '無鉛汽油98', '超級/高級柴油'])

# 繪製折線圖
plt.plot(df2['調價日期'], df2['無鉛汽油92'], label='無鉛汽油92')
plt.plot(df2['調價日期'], df2['無鉛汽油95'], label='無鉛汽油95')
plt.plot(df2['調價日期'], df2['無鉛汽油98'], label='無鉛汽油98')
plt.plot(df2['調價日期'], df2['超級/高級柴油'], label='超級/高級柴油')

# 設定標題，並使用中文字體
plt.title('調價日期與油價的關係', fontproperties=font)

# 設定 x 軸標籤，並使用中文字體
plt.xlabel('調價日期', fontproperties=font)

# 設定 y 軸標籤，並使用中文字體
plt.ylabel('價格', fontproperties=font)

# 設定圖例，並使用中文字體
plt.legend(prop=font)

# 設定 x 軸的刻度
plt.xticks(df2['調價日期'][::len(df2)//10], rotation=45)

plt.show()

# 將 DataFrame 輸出為 csv 檔
df2.to_csv('oil_price.csv', index=False)