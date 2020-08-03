
# Open this file.
f = open("mydata.txt", "r")

# Loop over each line in the file.
for line in f.readlines():

    # Strip the line to remove whitespace.
    line = line.strip()

    # Display the line.
    print(line)

    # Split the line.
    parts = line.split(",")

    # Display each part of the line, indented.
    for part in parts:
        print("   ", part)
