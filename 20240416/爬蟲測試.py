import requests

# 網站的URL
url = 'https://scweb.cwa.gov.tw/robots.txt'

# 發送GET請求
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    # 輸出robots.txt的內容
    print(response.text)
else:
    print("找不到robots.txt")