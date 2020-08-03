
# no problem this works well
# Siva can you try this without using the 
# syntax "dic.items()" i guess that is easy
# this dic.items() takes more performance

def dict_reverse_lookup(dic, value):
    new_dic = {v:list() for v in dic.values()}
    for k,v in dic.items():
        new_dic[v].append(k)

    return new_dic[value]

dic = {"key1":"value1","key2":"value2","key3":"value3","key4":"value2","key5":"value1" }

print(dict_reverse_lookup(dic,"value3"))
