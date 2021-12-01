from requests_html import HTMLSession

session = HTMLSession()

url = 'https://news.sina.com.cn/'

response= session.get(url=url)

print(response.html.xpath('//div[@id="ad_entry_b2"]/ul/li/a/text()'))
