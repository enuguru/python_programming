
def find_parity(num):
    parity = 0
    while num:
        if(num & 1 == 1):
            parity = parity ^ 1
        num = num >> 1
    return parity

var = int(input("Give a number"))
set_bits = find_parity(var)
if set_bits:
    print("It is odd parity")
else:
    print("It is even parity")
