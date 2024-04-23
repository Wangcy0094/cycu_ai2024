from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# 建立一個新的 Chrome 瀏覽器實例
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": os.getcwd(),  # 下載路徑設為當前工作目錄
    "download.prompt_for_download": False,  # 禁用下載確認對話框
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})

driver = webdriver.Chrome(options=chrome_options)

# 讓瀏覽器打開指定的 URL
driver.get('https://scweb.cwa.gov.tw/zh-tw/earthquake/data/')

# 等待網頁加載完成
wait = WebDriverWait(driver, 10)
csv_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[title="匯出地震資料 (地震活動彙整.csv)"]')))

# 點擊 CSV 下載連結
csv_link.click()

# 等待下載完成
import time
time.sleep(5)  # 等待 5 秒讓下載完成

# 關閉瀏覽器
driver.quit()

import shutil
# 找到下載的檔案名稱
downloaded_file = max([os.getcwd() + "\\" + f for f in os.listdir(os.getcwd())], key=os.path.getctime)

# 重新命名下載的檔案
shutil.move(downloaded_file, os.getcwd() + "\\earthquake.csv")