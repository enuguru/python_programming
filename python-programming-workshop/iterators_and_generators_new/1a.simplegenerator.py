
def fib():
    prev, curr = 0, 1
    while curr<100:
        yield prev
        prev, curr = curr, prev + curr

f = fib()
print(f)
for i in f:
    print(i)
#list(islice(f, 0, 10))
