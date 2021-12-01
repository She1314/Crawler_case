import json

dict1 = {'name': '佘俊男', 'age': 18}

print(json.dumps(dict1, indent=2))
dict2 = {'c': "C", 'a': "A"}
print(json.dumps(dict2, sort_keys=True))

with open('json_test.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(dict2, indent=4))