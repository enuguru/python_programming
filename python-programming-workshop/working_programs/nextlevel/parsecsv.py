
import csv
with open('eggs.csv', 'rb') as csvfile:
   file = csv.reader(eggs.csv)
   for row in file:
      print(', '.join(row))
