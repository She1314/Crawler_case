import requests
from requests.utils import dict_from_cookiejar

session = requests.session()

url = 'http://ptlogin.4399.com/ptlogin/login.do?v=1'

index_url = 'http://my.4399.com/forums/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36 "
}

data = {
    "username": "2397544674",
    "password": "RN8Tztg!rzh4NwK"
}

response1 = session.post(url=url, headers=headers, data=data)

response2 = session.get(url=index_url, headers=headers)

# print(response.cookies)

response2.encoding = 'utf-8'
print(response2.text)

