
import csv
with open('eggs.csv', newline='\n') as csvfile:
   file = csv.reader(csvfile, delimiter=',')
   for row in file:
      print(', '.join(row))

#>>> import csv
#>>> with open('eggs.csv', newline='') as csvfile:
#...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#...     for row in spamreader:
#...         print(', '.join(row))
#Spam, Spam, Spam, Spam, Spam, Baked Beans
#Spam, Lovely Spam, Wonderful Spam
