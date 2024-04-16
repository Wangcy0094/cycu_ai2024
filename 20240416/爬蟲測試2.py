# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# # 設定 ChromeDriver 的路徑
# webdriver_service = Service('/usr/local/bin/chromedriver')

# # 啟動瀏覽器並打開網頁
# driver = webdriver.Chrome(service=webdriver_service)
# driver.get('https://scweb.cwa.gov.tw/zh-tw/earthquake/data/')

# # 獲取 CSV 檔案的 URL
# url_csv = driver.execute_script('return urlCSV;')

# # 下載 CSV 檔案
# response = requests.get(url_csv)
# with open('earthquake_data.csv', 'w') as f:
#     f.write(response.text)

# # 關閉瀏覽器
# driver.quit()




# from requests_html import HTMLSession

# # 建立一個新的會話
# session = HTMLSession()

# # 載入網頁
# r = session.get('https://scweb.cwa.gov.tw/zh-tw/earthquake/data/')

# # 執行 JavaScript，並等待 5 秒以確保 JavaScript 有足夠的時間來生成動態內容
# r.html.render(sleep=5)

# # 獲取 CSV 檔案的 URL
# url_csv = r.html.find('#urlCSV', first=True).attrs['value']

# # 下載 CSV 檔案
# response = session.get(url_csv)
# with open('earthquake_data.csv', 'w') as f:
#     f.write(response.text)


# import scrapy
# import re
# from requests_html import HTMLSession

# # 建立一個新的會話
# session = HTMLSession()

# # 載入網頁
# r = session.get('https://scweb.cwa.gov.tw/zh-tw/earthquake/data/')
# # 從 JavaScript 代碼中提取 URL
# match = re.search(r"var urlCSV = '([^']+)'", r.html.html)
# if match:
#     url_csv = match.group(1)

# class MySpider(scrapy.Spider):
#     name = 'myspider'
#     start_urls = [f'https://scweb.cwa.gov.tw{url_csv}']

#     def parse(self, response):
#         with open('earthquake_data.csv', 'w') as f:
#             f.write(response.text)

# from scrapy.crawler import CrawlerProcess

# # 創建一個新的爬蟲進程
# process = CrawlerProcess()

# # 添加你的爬蟲到進程
# process.crawl(MySpider)

# # 開始爬蟲進程
# process.start()

# print('---------------------------------')

var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://scweb.cwa.gov.tw/zh-tw/earthquake/data/', true);
xhr.responseType = 'blob';

xhr.onload = function(e) {
    if (this.status == 200) {
        var blob = new Blob([this.response], {type: 'text/csv'});
        var downloadUrl = URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = downloadUrl;
        a.download = 'data.csv';
        document.body.appendChild(a);
        a.click();
    }
};

xhr.send();