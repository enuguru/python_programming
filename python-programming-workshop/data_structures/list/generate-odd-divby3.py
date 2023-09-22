#generate odd numbers divisible by 5 between 1 and 100
def generate_odd_numbers_divby5():
    odd_numbers_divby5 = []
    for num in range(1, 100):
        if num % 2 != 0 and num % 5 == 0:
            odd_numbers_divby5.append(num)
    return odd_numbers_divby5   

print(generate_odd_numbers_divby5())


