
# Siva the answer is nice, you have used the 
# syntax provided in python itself which is
# dic.items()  no issues this is fine
# can you try without using the dic.items() syntax
# with just plain logic?

dic = {"key1":"value1","key2":"value2","key3":"value3","key4":"value2","key5":"value1" }


new_dic = {v:list() for v in dic.values()}

for k,v in dic.items():
    new_dic[v].append(k)

print(dic)
print(new_dic)
