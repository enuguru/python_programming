
#notes on how the rsplit works

#Rsplit. Usually rsplit() is the same as split. The only difference occurs when the 
#second argument is specified. This limits the number of times a string is separated.

#So:When we specify 3, we split off only three times from the right. This is the 
#maximum number of splits that occur.

#Tip:The first element in the result list contains all the remaining, non-separated 
#string values. This is unprocessed data.

# Data.
s = "Buffalo;Rochester;Yonkers;Syracuse;Albany;Schenectady"

# Separate on semicolon.
# ... Split from the right, only split three.
cities = s.rsplit(";", 3)

# Loop and print.
for city in cities:
    print(city)
