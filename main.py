import requests
import json

request = []
client_id = '8e7e753658d463eb9939'
client_secret = '0cee12e62a8e7a043e8ceaac37f1de49'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)
# достаем токен
token = j["token"]
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
with open("dataset_24476_4.txt", 'r', encoding='utf-8') as k:
    n = k.read().splitlines()
for nm in n:
    r = requests.get(f"https://api.artsy.net/api/artists/{nm}", headers=headers)

# разбираем ответ сервера
    j = json.loads(r.text)
    request.append(f"{j['birthday']} {j['sortable_name']}")
# получаем список дат с именами через пробел и сортируем по дате и имени
print(request)
request.sort()
# выводим имена
for n in request:
    print(n[5:])
