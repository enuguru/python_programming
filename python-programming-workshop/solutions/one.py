
number = int(input("Give a number))
for val in range(1,101):
    if number % val == 0:
        print(val, end = " ")
