import sys
a =10
print(sys.getrefcount(a)) #17
 
def func(b):
    print(sys.getrefcount(a)) #19
 
func(a)
print(sys.getrefcount(a)) #17
