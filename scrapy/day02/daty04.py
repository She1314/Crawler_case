import requests
from requests.utils import dict_from_cookiejar

session = requests.session()
url = 'https://accounts.douban.com/j/mobile/login/basic'
index_url = 'https://www.douban.com/'
headers_index = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
    'Referer': "https://accounts.douban.com/passport/login_popup?login_source=anony",
}

data = {
    "name": "19856917553",
    "password": "20196768Xd666"
}
# response = requests.post(url=url, headers=headers, data=data)

response1 = session.post(url=url, headers=headers, data=data, )
response2 = session.get(url=index_url, headers=headers_index)
print(response2.text)
