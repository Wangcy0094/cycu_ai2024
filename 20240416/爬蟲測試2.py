from selenium import webdriver

# 建立一個新的瀏覽器實例
driver = webdriver.Chrome()

# 載入網頁
driver.get('https://scweb.cwa.gov.tw/zh-tw/earthquake/data/')

# 執行 JavaScript 來獲取 js_id
js_id = driver.execute_script('return urlCSV.split("/")[5];')

# 建立 CSV 檔案的 URL
url_csv = f'https://scweb.cwa.gov.tw/zh-tw/earthquake/csv/{js_id}'

# 下載 CSV 檔案...
driver.get(url_csv)