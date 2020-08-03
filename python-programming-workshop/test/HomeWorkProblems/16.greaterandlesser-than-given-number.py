

# Count the number of elements in a list that are greater
# than or equal to some minimum number and less that or equal
# to some maximum number for example, the list of numbers can
# be 12, 5, 23, 79, 63, 11, 7, 6, 115, 129
# minimum is 10 and maximum is 100]


newlist = [12, 5, 23, 79, 63, 11, 7, 6, 115, 129]

minimum = 10
maximum = 100

for number in newlist:
    if(number > minimum and number < maximum):
        print(number)