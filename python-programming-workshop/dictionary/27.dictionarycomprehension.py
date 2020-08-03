
one = {i: i**2 for i in range(5)}
print(one)


d = {}
for i in range(5):
    d[i] = i**2
print(d)


def gen():
    for i in range(5):
        yield i

print(gen)
p = gen()
p = gen()
print(p)
print(gen)


gen = (i for i in range(5))
p = next(gen)
print(p)
q = next(gen)
print(q)
one = list(gen)
print(one)
#q = next(gen)
#print(q)
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#StopIteration


prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }
# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names }
print(p1)
print(p2)
