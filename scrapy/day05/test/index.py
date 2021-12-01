from requests_html import HTMLSession
from lxml import etree
session = HTMLSession()
import re
url = 'https://pic.netbian.com/e/search/result/?searchid=45'
image_url = session.get(url=url).text
content = etree.HTML(image_url)
print(content.xpath('//div[@class="slist"]//a/img/@src'))



