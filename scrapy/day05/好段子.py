import os
import time

from requests_html import HTMLSession
import re
import json

page = input("请输入你要爬取结束的页数")

content = {}
session = HTMLSession()
for k in range(1, int(page)+1):
    url = f'http://www.haoduanzi.com/category/?1-{k}.html'
    response = session.get(url=url)
    response.encoding = 'utf-8'

    # print(response.text)
    content_title = re.findall('<h2 class="s2">(.*?)</h2>', response.text, re.S)
    content_text = re.findall('<div class="content"><a href=".*?" target="_blank">(.*?)</a></div>', response.text, re.S)
    print(content_title)
    print(len(content_text))
    for i in range(len(content_title)):
        content[content_title[i]] = content_text[i]
    # print(re.findall('<h2 class="s2">(.*?)</h2>', content_title))
    # print(content_title, content_text)
    content = {key: re.sub(r'\s|</P><P>', '', value) for key, value in content.items()}
    content = json.dumps(content, indent=4, ensure_ascii=False)
    print(content)
    time.sleep(3)
    file = os.getcwd() + r'\好段子'
    print(file)
    if not os.path.exists(file):
        os.mkdir(file)
    with open(file + rf'\好段子第{k}页.json', 'w', encoding='utf-8') as f:
        f.write(content)
    content = {}

