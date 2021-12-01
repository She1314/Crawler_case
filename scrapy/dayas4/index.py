from xpinyin import Pinyin
import requests
import json
p = Pinyin()

param = input("请输入你要搜索的数据：")

pinyin_param = p.get_pinyin(chars=param, splitter='')
url = f'https://699pic.com/search/getKwInfo?kw={param}'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
}
response = requests.get(url=url, headers=headers)

dict_verify_key = response.json().get("data")["pinyin"]

print(url)
print(dict_verify_key)
#
# # 模拟请求成功

index_url = f"https://699pic.com/tupian/{dict_verify_key}.html"

print(index_url)
# response_index_url = requests.get(url=index_url, headers=headers)
#
# print(response_index_url.text)

