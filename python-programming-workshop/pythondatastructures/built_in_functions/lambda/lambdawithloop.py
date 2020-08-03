
# If we need to perform loops within a lambda, we can also embed 
# things like map calls and list comprehension expressions.

import sys

fullname = lambda x: list(map(sys.stdout.write,x))
f = fullname(['Wassily ', 'Wassilyevich ', 'Kandinsky'])
print(f)

fullname = lambda x: [sys.stdout.write(a) for a in x]
t = fullname(['Wassily ', 'Wassilyevich ', 'Kandinsky'])
print(t)
