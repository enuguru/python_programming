
for num in range(1,21):
    num = num * num;
    print(num,end=" ")
print()


print([x*x for x in range(1,21)])


print([num for num in range(1,201) if (num%3==0) and (num%5==0)])
