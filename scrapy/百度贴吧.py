import requests
import os
number = int(input("请输入你要爬取的页数"))
item = input("请输入你要查询的信息")
for i in range(1, number + 1):
    url = f"https://tieba.baidu.com/f?kw={item}&ie=utf-8&pn={50 * i - 50}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/94.0.4606.81 Safari/537.36 "
    }
    response = requests.get(url=url, headers=headers)
    print(response.request.headers)
    os_path = os.getcwd() + f"/{item}"
    if not os.path.exists(os_path):
        os.mkdir(os_path)
    with open(os_path + f"/{item}第{i}页信息.html", 'w', encoding='utf-8') as f:
        f.write(response.text)
