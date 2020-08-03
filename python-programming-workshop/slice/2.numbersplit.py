
numbers = "100.200.50"

# Split apart the numbers.
myvalues = numbers.split(".")
print(myvalues)
# Loop over strings and convert them to integers.
# ... Then sum them.
total = 0
for var in myvalues:
    print(var,end=" ")
print()
for var in myvalues:
    total = total + int(var)
print(total)
