
# Read a collections of integers from the user which can
# be negative numbers, zeros or positive numbers.
# Display all the of the negative numbers, followed by all
# of the zeros, followed by all of the positive integers.
# do all this with lists

newlist = []

for loopcount in range(7):
    number = input("Give a value")
    newlist.append(number)

print(sorted(newlist))
