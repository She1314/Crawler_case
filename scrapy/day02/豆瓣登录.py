import requests
from requests.utils import dict_from_cookiejar
url = 'https://www.douban.com/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36 ",
    'Cookie': 'll="118192"; bid=Yf9Z0CrB_8k; _pk_ses.100001.8cb4=*; __utma=30149280.538038249.1637484942.1637484942.1637484942.1; __utmc=30149280; __utmz=30149280.1637484942.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.25047; dbcl2="250472406:3u4XVOIDckI"; ck=s28X; _pk_id.100001.8cb4=416619f9cfc8bc96.1637484940.1.1637488881.1637484940.; __utmt=1; __utmb=30149280.24.10.1637484942',
}
# cookies = 'll="118192"; bid=Yf9Z0CrB_8k; _pk_ses.100001.8cb4=*; ' \
#           '__utma=30149280.538038249.1637484942.1637484942.1637484942.1; __utmc=30149280; ' \
#           '__utmz=30149280.1637484942.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap_v=0,6.0; push_noty_num=0; ' \
#           'push_doumail_num=0; __utmv=30149280.25047; dbcl2="250472406:3u4XVOIDckI"; ck=s28X; ' \
#           '_pk_id.100001.8cb4=416619f9cfc8bc96.1637484940.1.1637488001.1637484940.; __utmb=30149280.20.10.1637484942 '

# cookies_dict = {}
# for i in cookies.split(';'):
#     cookies_dict[i.split("=")[0]] = i.split("=")[-1]

response = requests.get(url=url, headers=headers)

print(response.text)

