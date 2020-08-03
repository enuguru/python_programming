

#data = [x for x in x>1]
#print(data)
#lazy_squares = (x*x for i in data)
#lazy_squares

gen = (x/2 for x in range(20))
print(gen)

for i in gen:
    print(i)
