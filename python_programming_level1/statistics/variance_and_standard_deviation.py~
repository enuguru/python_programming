# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

val = int(input())
numbers = list(map(int,input().split()))
squares = 0; stad = 0
mean = sum(numbers) / val
for num in numbers:
    squares = squares + ((num-mean) * (num-mean))
stad = math.sqrt(squares/val)
print(stad)
print(squares/val)
