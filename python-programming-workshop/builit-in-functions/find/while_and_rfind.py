
#Python program that uses rfind, while

# rfind first argument is a string and second one is where to end and 
#3rd one is where to start

value = "this picture is a cat picture is cat picture"

# Start with length of string.
i = len(value)

while True:
    # Find rightmost string in this range.
    i = value.rfind("picture", 0, i)

    # Check for not found.
    if i == -1: break
    print(i)
