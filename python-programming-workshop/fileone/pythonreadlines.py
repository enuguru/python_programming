
# Open a file on the disk.
f = open("perls.txt", "r")

# Print all its lines.
for line in f.readlines():
    # Modify the end argument.
    print(line, end="")
