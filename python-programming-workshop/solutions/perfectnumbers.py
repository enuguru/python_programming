
for num in range(2,100001):
    total = 0
    for val in range(1,num):
        if num % val == 0:
            total = total + val
    if total == num:
        print(num,end=" ")
print()
