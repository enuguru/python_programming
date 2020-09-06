
# n is the numbers lines
# the next n lines give one key and one value
# example below
# 3
# guru 89
# karthik 100
# BadriNarayanan 100


n = int(input())
name_numbers = [input().split() for _ in range(n)]
print(name_numbers)
phone_book = {k: v for k,v in name_numbers}
print(phone_book)
