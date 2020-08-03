

number = int(input("Give a number"))

for val in range(2,number):
    if number % val == 0:
        print(val,end= " ")
print()


val = [val for val in range(2,number) if number % val ==0]
print(val)


def find_factors(n):
    for val in range(2,number):
        if number % val == 0:
            print(val,end= " ")
    print()

find_factors(number)



