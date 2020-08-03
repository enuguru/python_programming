
with open("words.txt") as openfile:
   for line in openfile:
       for part in line.split():
           if "color" in part:
               print(part)
               print(line)
