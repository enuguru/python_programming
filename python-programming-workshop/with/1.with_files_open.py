
files = []
for x in range(10000):
    f = open('foo.txt', 'w')
    f.close()
    files.append(f)
