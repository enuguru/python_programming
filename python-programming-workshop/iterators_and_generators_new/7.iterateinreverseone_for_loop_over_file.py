
# Print a file backwards
f = open("1.iter_function.py","r")
for line in reversed(list(f)):
    print(line, end='')
