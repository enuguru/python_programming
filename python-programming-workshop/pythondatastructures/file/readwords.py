
with open('words.txt','r') as f:
    for line in f:
        for word in line.split():
           print(len(word))
           print(word)
      
