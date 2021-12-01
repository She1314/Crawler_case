import urllib.request
from urllib import request
import requests


def handle_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def page_func():
    page_start = int(input("请输入你要开始的页数："))
    page_end = int(input("请输入你要结束的页数："))
    if page_end <= 13 and page_start >= 1:
        for i in range(page_start, page_end + 1):
            url = f"https://www.qiushibaike.com/imgrank/page/{i}/"
            request_url = handle_request(url)
            content = urllib.request.urlopen(request_url).read().decode()
            return content
    else:
        return "页数较多, 无法完成"


if __name__ == '__main__':
    print(page_func())
