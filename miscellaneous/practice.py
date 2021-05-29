
val = int(input())

numbers = sorted(list(map(int,input().split())))

mean = sum(numbers)/val
print(mean)

if val%2 == 0:
    median = numbers[(val//2)-1] + numbers[(val//2)] / 2
else:
    median = numbers[(val//2)+1]
print(median)

mode = max(numbers,key=numbers.count)
print(mode)
