import string
import functools
s="314"
t="AZ"
#print(functools.reduce(lambda running_sum,c:running_sum*10+string.digits.index(c),0,s[s[0]=='-']))
print(functools.reduce(lambda result,c:result*26+ord(c)-ord('A')+1,t,0))

