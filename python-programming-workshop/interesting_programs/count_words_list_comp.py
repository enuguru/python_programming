
words = list(['calm','simple','cool','great','cool','simple'])
dct = {}
{w: 1 if w not in dct and not dct.update({w: 1}) else dct[w] + 1 if not dct.update({w: dct[w] + 1}) else 1 for w in words}
print(dct)
