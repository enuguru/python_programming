

import csv

#Open CSV file.
with open("input.csv", newline="") as f:

    # Specify delimiter for reader.
    r = csv.reader(f, delimiter=",")

    # Loop over rows and display them.
    for row in r:
        print(row)
