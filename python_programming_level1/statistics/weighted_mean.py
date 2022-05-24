# Enter your code here. Read input from STDIN. Print output to STDOUT

val = int(input())
arraylist = list(map(int,input().split()))
weightlist = list(map(int,input().split()))
mysum = 0
for i in range(val): 
    mysum = mysum + (arraylist[i] * weightlist[i])
print(round(mysum/sum(weightlist),1))
