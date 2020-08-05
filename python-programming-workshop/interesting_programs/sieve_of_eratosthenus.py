
l = range(2, 101)
print(sorted(set(l).difference(a for i in l for a in l if a!=i and a%i == 0)))
