
# this program converts an excel column id to an integer
import functools

col = input("enter a valid excel column id ").upper()
# 0 goes to ret, col goes to c variable
# it is reverse in reduce function

print(functools.reduce(lambda ret,c:ret*26+ord(c)-ord('A')+1,col,0))


