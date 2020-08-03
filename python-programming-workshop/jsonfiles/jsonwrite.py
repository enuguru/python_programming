import json

obj = {u"answer": [42.2], u"abs": 42}
print(json.dumps(obj))
with open('data.txt', 'w') as outfile:
    json.dump(obj, outfile)
