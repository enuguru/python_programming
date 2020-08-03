
#!/usr/bin/python
file=open("words.txt")
wordcount= {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print(len(wordcount))
for theword,thewordcount in wordcount.items():
    print(theword, thewordcount)
