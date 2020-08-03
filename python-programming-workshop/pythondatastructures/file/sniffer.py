

#Python program that uses Sniffer

import csv

# Open the file.
with open("input.csv") as f:

    # Get dialect from Sniffer.
    # ... Pass a sample to sniff.
    dialect = csv.Sniffer().sniff(f.read(1024))

    # Seek to beginning.
    f.seek(0)

    # Read file and print its rows.
    r = csv.reader(f, dialect)
    for row in r:
        print(row)
