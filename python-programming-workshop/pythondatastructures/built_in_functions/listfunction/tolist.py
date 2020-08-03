
import array

a = array.array('I', [1, 2, 3, 4, 5])
b = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
c = array.array('b', [5, 3, 1])
x = memoryview(a)
y = memoryview(b)
x == a == y == b
x.tolist() == a.tolist() == y.tolist() == b.tolist()
print(x)
print(a)
print(y)
print(b)
z = y[::-2]
z == c
z.tolist() == c.tolist()
