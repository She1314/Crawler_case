str1 = '<a href="/renwu/fuhao/shishi_view_115.html" title="马化腾" target="_blank" class="cty"><span class="fl"><img ' \
       'src="https://img.phb123.com/uploads/fuhao/1/8352f1919ca2930cae5f34dce8ef3763.jpg" alt="马化腾" ' \
       'width="70"></span><p>马化腾</p></a> '

import re

compile = re.compile('.*?title="(.*?)".*?')

print(re.findall(compile, str1))



