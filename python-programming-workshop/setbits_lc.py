
x = 34567
print(sum(1 for i in range(0,16) if x & (1<<i)>0))
