
import functools
character=input()#'Z'  #602
result=functools.reduce(lambda x,c:x*26+ord(c)-ord('A')+1,character,0)
print(result)
