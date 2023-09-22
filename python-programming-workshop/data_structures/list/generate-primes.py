# generate prime numbers between 1 and 100
# prime numbers are numbers that are divisible by 1 and itself
# 1 is not a prime number
def generate_primes():
    primes = []
    for num in range(2, 100):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

print(generate_primes())
