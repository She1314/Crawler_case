from requests_html import HTMLSession

session = HTMLSession()

url = 'https://yuedu.baidu.com/book/list/0?fr=indextop'
response = session.get(url=url)

# print(response.html.text)

print(response.html.xpath('//div[@class="booklist-inner clearfix"]/div/a/img/@alt'))