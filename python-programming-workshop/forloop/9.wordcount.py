
#!/usr/bin/python
file=open("words.txt","r+")
wordcount= {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1 # wordcount[word] = wordcount[word] + 1
for theword,thewordcount in wordcount.items():
    print(theword, thewordcount)
