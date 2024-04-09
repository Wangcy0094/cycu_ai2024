import requests

# Replace with the actual URL of the CSV file
csv_url = 'https://scweb.cwa.gov.tw/zh-tw/earthquake/csv/2024%E5%B9%B44%E6%9C%88'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(csv_url, headers=headers)

# Ensure the request was successful
if response.status_code == 200:
    with open('earthquake_data.csv', 'wb') as f:
        f.write(response.content)
else:
    print(f'Error downloading CSV file: {response.status_code}')