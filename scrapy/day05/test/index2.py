import re

content = """

I read a good story that told about a married couple. The wife read from a magazine that listing the 
unsatisfied problems between the couples could help them to keep their marriage better. So they listed the problems 
on a separated room. The wife was the first to talked about the unsatisfied problems, it surprised the husband that 
she got three pages. When it was the turn for the husband to read the problems, he got nothing in the paper. He told 
his wife that she was the most perfect girl in his heart and he didn’t want the girl change a. thing. """
print(re.split(r'\W', content))