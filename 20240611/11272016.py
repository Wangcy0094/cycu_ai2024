import requests

# TOKEN_NOTIFY = 'iSWyrnS4AFuwUU9MTyx3z1rZ65QjSZeRW8Dbm3oZpK0'
# message = '王振宇'

# rd = requests.post(
#     "https://notify-api.line.me/api/notify",
#     headers={"Authorization": f"Bearer {TOKEN_NOTIFY}"},
#     data={"message": message}
# )

TOKEN_NOTIFY = 'PDcpmD5Go2CSFmDlAqwDkEWxsiSnuV3qpSv72h8vLAP'
message = '唯一支持'
image_path = 'C:\\Users\\User\\Desktop\\AI\\99.jpg'

with open(image_path, 'rb') as image_file:
    rd = requests.post(
        "https://notify-api.line.me/api/notify",
        headers={"Authorization": f"Bearer {TOKEN_NOTIFY}"},
        data={"message": message},
        files={"imageFile": image_file}
    )

# 檢查請求是否成功
if rd.status_code != 200:
    print(f"傳送失敗，錯誤碼：{rd.status_code}")
    print(f"錯誤訊息：{rd.text}")
else:
    print("傳送成功")