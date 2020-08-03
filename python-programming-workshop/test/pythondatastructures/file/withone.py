


name="perls.txt"

# Open the file in a with statement.
with open(name) as f:
    print(f.readline(), end="")

# Repeat.
with open(name) as f:
    print(f.readline(), end="")
