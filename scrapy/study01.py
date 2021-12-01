import requests

url = "https://www.google.com.hk/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36 "
}

response = requests.get(url=url, headers=headers)

print(type(response))
