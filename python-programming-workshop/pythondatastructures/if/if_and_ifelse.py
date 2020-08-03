

#Python program that uses if-statements

def test(n):
    if n == 0:
        print("None")
    elif n < 0:
        print("Low")
    else:
        # Handle values greater than zero.
        if n > 100:
            print("Out of range")
        else:
            print("High")


test(-1)
test(0)
test(1)
test(1000)
