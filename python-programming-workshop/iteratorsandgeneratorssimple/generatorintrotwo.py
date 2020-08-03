
val = (sum(i*i for i in range(10)))
valone = (i*i for i in range(10))
for i in valone:
    print(i)
print(val)

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec))) #finds the dot product

from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
print(sine_table)

page = open("myfile.txt")
unique_words = set(word  for line in page  for word in line.split())
print(unique_words)

#valedictorian = max((student.gpa, student.name) for student in graduates)
#print(valedictorian)

data = 'playing golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))
