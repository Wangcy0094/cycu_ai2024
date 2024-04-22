from selenium import webdriver
import time

# 建立一個新的 Chrome 瀏覽器實例
driver = webdriver.Chrome('./chromedriver')

# 讓瀏覽器打開指定的 URL
driver.get('https://scweb.cwa.gov.tw/zh-tw/earthquake/data/')

# 等待網頁加載完成
time.sleep(5)

# 找到 CSV 下載連結並點擊
csv_link = driver.find_element_by_xpath('//a[@class="BaSet csv"]')
csv_link.click()

# 在這裡添加你的爬蟲程式碼...

# 關閉瀏覽器
driver.quit()