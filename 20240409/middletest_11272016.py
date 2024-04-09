import requests

# The URL of the CSV file
url = 'https://scweb.cwa.gov.tw/zh-tw/earthquake/csv/2024%E5%B9%B44%E6%9C%88'

# Send a GET request to the URL
response = requests.get(url)

# Make sure the request was successful
response.raise_for_status()

# Write the contents of the response to a CSV file
with open('data.csv', 'wb') as f:
    f.write(response.content)