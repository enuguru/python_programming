
import csv
with open('sample.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
