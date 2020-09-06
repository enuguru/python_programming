
# this program converts an excel column id to an integer
import functools

col = input("enter a valid excel column id ").upper()

print(functools.reduce(lambda ret,c:ret*26+ord(c)-ord('A')+1,col,0))
