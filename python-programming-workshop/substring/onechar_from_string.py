
value = "web"

# Loop over every index in string.
for index in range(0, len(value)):

    # Get one-character substring.
    char = value[index]

    # Display substring.
    print(char)

    # Test substring.
    if char == "w":
        print(True)
