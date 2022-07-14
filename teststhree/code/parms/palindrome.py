# parms/palindrome.py

def is_palindrome(value):
    value = value.replace(' ', '').lower()
    split = len(value) // 2

    if len(value) % 2 == 0:
        # Even length
        left = value[:split]
        right = value[split:]
    else:
        # Odd length
        left = value[:split]
        right = value[split+1:]

    return left == right[::-1]
