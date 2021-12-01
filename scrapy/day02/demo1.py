import re
params = 'i dsnjds sjkdhsa!     jhsdis s  ki ji'
num = ''

print(re.split(r'\W', params))
print(params.split('!'))

for b, count in enumerate([(1, 2), (2, 3), (4, 5)]):
    print(b, count)

