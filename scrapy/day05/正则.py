content = """
<div class="book-info fl">
<h3>NO.1</h3>
<h4>
<a href="//book.qidian.com/info/1027669580/" target="_blank" 
data-eid="qd_A117" data-bid="1027669580">星门</a>
</h4>
<p class="digital f16">销量冠军</p>
<p class="author">
<a class="type" href="//www.qidian.com/xuanhuan/" target="_blank">玄幻</a>
<i>·</i>
<a class="writer" href="//my.qidian.com/author/3228548/" target="_blank">老鹰吃小鸡</a></p></div> 
"""
import re

# print(re.split(r'\W', content))
print(re.findall(r'<h3>.*</div>', content, re.S))
print(re.findall(r'<h(\d)>', content))
