
def count_bits(num):
    count = 0
    while num:
        count = count ^ 1
        num = num & (num-1)
    return count

var = int(input("Give a number"))
set_bits = count_bits(var)
if set_bits:
    print("It is odd parity")
else:
    print("It is even parity")
