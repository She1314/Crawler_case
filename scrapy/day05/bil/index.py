from requests_html import HTMLSession
import re
import os

session = HTMLSession()

url = 'https://www.bilibili.com/video/BV1Fh411t7xi'

headers = {
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

# phone_url = session.get(url=url).text
#
# Bv_url = re.findall(r'<meta data-vue-meta="true" itemprop="url" content="(.*?)">', phone_url)[0]
#
# print(Bv_url)
response_phone = session.get(url=url, headers=headers).text
# print(response_phone)
# url_compile = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
#
#
# video_url = re.findall(url_compile, response_phone)
#
# list_video_url = list(set(video_url))
#
# print(list_video_url)

video_url = re.findall(r"readyVideoUrl: '(.*?)'", response_phone)[0]
dianzan_num = re.findall(r'<i class="iconfont dianzan"></i> <span>(.*?)</span>', response_phone)[0]
shoucang_num = re.findall(r'<i class="iconfont icon_fav"></i> <span>(.*?)</span></span>', response_phone)[0]
print(shoucang_num)
print(dianzan_num)
file = os.getcwd() + r'\哔哩视频'

# if not os.path.exists(file):
#     os.mkdir(file)
# with open(file + r'\[JJAL国志 重启] 赤巾军.mp4', 'wb') as f:
#     f.write(session.get(url=video_url).content)

print(video_url)
