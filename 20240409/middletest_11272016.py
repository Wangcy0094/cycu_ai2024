import requests

# Replace with the actual URL of the CSV file
csv_url = 'https://scweb.cwa.gov.tw/zh-tw/earthquake/csv/2024%E5%B9%B44%E6%9C%88'

response = requests.get(csv_url)

# Ensure the request was successful
if response.status_code == 200:
    with open('earthquake_data.csv', 'wb') as f:
        f.write(response.content)
else:
    print(f'Error downloading CSV file: {response.status_code}')
