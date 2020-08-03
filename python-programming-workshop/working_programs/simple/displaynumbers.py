
## python program to display the numbers in ascending order using list ##

#integers = [34, 2, -1, 24, 35, 0, 0, -24, -12]

integers = []
count = 0
while(count < 4):
    number = int(input(" Give a number : "))
    integers.append(number)
    count = count + 1

print(sorted(integers))
