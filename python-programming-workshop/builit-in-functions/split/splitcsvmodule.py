


# Data.
s = "Buffalo;Rochester;Yonkers;Syracuse;Albany;Schenectady"

# Separate on semicolon.
# ... Split from the right, only split three.
cities = s.rsplit(";", 3)

# Loop and print.
for city in cities:
    print(city)
