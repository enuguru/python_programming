
# 0 1 1 2 3 5 8 13 21 34 55 89 ......

def fibonacci(n): 
    a = 0
    b = 1
    if n < 1: 
        print("Incorrect input") 
    elif n == 1: 
        print(a)
    elif n == 2: 
        print(a,b)
    else: 
        print("0 1",end=" ")
        for i in range(3,n+1): 
            c = a + b 
            print(c,end= " ")
            a = b 
            b = c 
  
# Driver Program 
  
fibonacci(5)
print()
