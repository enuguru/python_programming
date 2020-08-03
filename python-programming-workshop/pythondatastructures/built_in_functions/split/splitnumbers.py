
# A tuple can be specified with no parentheses.

numbers = "100,200,50"

# Split apart the numbers.
values = numbers.split(",")

# Loop over strings and convert them to integers.
# ... Then sum them.
total = 0
for value in values:
    total += int(value)

print(total)
