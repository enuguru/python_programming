
def reverseLookup(data, value):
    keys = []
    for key in data:
        if(data[key] == value):
            keys.append(key)
    return keys

dict = {"Karthick":1000000, "Guru" : 23, "Ravi": 1000000 }
answer = reverseLookup(dict,1000000)

print(answer)
