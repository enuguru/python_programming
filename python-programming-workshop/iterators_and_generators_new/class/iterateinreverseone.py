
# Print a file backwards
f = open('iterateinreverseone.py')
for line in reversed(list(f)):
    print(line, end='')
