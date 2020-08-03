
import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False


def get_primes():
    number = 11
    while True:
        if is_prime(number):
            print(number)
            yield number
        number += 1

get_primes()
