import dis
import sys
 
print(compile("sys.getrefcount(1556778)", '', 'single').co_consts)
print(dis.dis(compile("sys.getrefcount(1556778)", '', 'single')))
print(sys.getrefcount(1556778))
