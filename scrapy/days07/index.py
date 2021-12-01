from requests_html import HTMLSession
import re, csv

session = HTMLSession()

url = 'https://www.phb123.com/renwu/fuhao/shishi_1.html'

response = session.get(url=url)

compile = re.compile('<td class="xh">(.*?)<.*?title="(.*?)".*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?title="(.*?)"', re.S)

print(re.findall(compile, response.text))