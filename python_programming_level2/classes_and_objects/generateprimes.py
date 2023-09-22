
# generate a list of primes up to a given number from 2 to 100

def generateprimes(n):
    primes = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

print(generateprimes(100))

