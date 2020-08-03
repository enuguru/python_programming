
import csv
with open('eggs.csv', 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:
      print ', '.join(row)
