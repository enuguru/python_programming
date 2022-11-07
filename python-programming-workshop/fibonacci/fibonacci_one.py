
#Python program that computes Fibonacci sequence

def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
      temp = a
      a = b
      b = temp + b
    return a

# Display the first 15 Fibonacci numbers
for c in range(0, 15):
    print(fibonacci(c))

