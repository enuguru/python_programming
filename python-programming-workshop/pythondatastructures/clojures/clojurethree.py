
import math
def prepare_factor(max):
    # Creating a prime table is time-consuming.
    primes = [i for i in range(2, max) if primes[i] == 1]

    def factor(num):
        while primes[i] ** 2 <= num:
            if num % primes[i] == 0:
                list.append(primes[i])
                num //= primes[i]
            else:
                i += 1

    return factor

factor = prepare_factor(1000)
print(factor(100)) # print [2, 2, 5, 5]
