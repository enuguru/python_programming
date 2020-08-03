import json
obj_json = u'{"answer": [42.2], "abs": 42}'
obj = json.loads(obj_json)
print(repr(obj))
