

#Python program that validates input

while True:
    try:
        # Get input with prompt.
        code = input("Code: ")
        # Attempt to parse input.
        value = int(code)
        break;
    except:
        print("Invalid code")

print("Value:", value)
