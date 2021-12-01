from requests_html import HTMLSession

session = HTMLSession()

url = 'https://699pic.com/tupian/daxiang.html'

response = session.get(url=url)

for i in response.html.xpath('//div[@class="list"]/a/@title'):
    print(i)