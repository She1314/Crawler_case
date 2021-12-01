import requests
sum1 = 2
result = 0
under = 1
for i in range(20):
    result += sum1 / under
    sum1 = sum1 + under
    under = sum1 - under
print(result)