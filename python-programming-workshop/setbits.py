
num = 67

count = 0
while(num):
    if((num & 1) == 1):
        count = count + 1
    num = num >> 1
print(count)
