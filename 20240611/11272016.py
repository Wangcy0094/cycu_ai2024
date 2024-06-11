import requests

# TOKEN_NOTIFY = 'iSWyrnS4AFuwUU9MTyx3z1rZ65QjSZeRW8Dbm3oZpK0'
# message = '王振宇'

# rd = requests.post(
#     "https://notify-api.line.me/api/notify",
#     headers={"Authorization": f"Bearer {TOKEN_NOTIFY}"},
#     data={"message": message}
# )


TOKEN_NOTIFY = 'iSWyrnS4AFuwUU9MTyx3z1rZ65QjSZeRW8Dbm3oZpK0'
message = '測試'
image_path = 'C:\\Users\\User\\Desktop\\AI\\image.png'

with open(image_path, 'rb') as image_file:
    rd = requests.post(
        "https://notify-api.line.me/api/notify",
        headers={"Authorization": f"Bearer {TOKEN_NOTIFY}"},
        data={"message": message},
        files={"imageFile": image_file}
    )