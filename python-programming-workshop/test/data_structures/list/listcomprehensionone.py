
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
p = [n for n in mylist if n > 0]
print(p[2])
print(p)

x=[n for n in mylist if n < 0]
print(x)

pos = (n for n in mylist if n > 0)
#print(pos)
for x in pos:
    print(x)
