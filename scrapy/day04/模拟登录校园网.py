import requests
from requests.utils import dict_from_cookiejar

session = requests.session()
url = 'https://sso.chzu.edu.cn/login'
index_url = 'https://my0.chzu.edu.cn/home'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
    # 'referer': "https://sso.chzu.edu.cn/login?service=https%3A%2F%2Fmy0.chzu.edu.cn%2Fcas%2Fvalidate&sn=undefined",
}
response = requests.get(url=index_url, headers=headers)

# response1 = session.post(url=url, headers=headers, data=data, )
# response2 = session.get(url=index_url, headers=headers_index)
print(response.text)


