
# Has numbers on left and right, and some syntax.
value = "50342=Data,231"

# Strip all digits.
# ... Also remove equals sign and comma.
result = value.strip("0123456789=,")
print(result)
