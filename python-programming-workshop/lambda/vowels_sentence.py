import itertools
from collections import Counter
s=input()
vowels='aeiou'
mylist=[i for i in s if i in vowels]
d=Counter(mylist)
print(d)
for key,value in d.items():
    if value>1:
        print(key)

