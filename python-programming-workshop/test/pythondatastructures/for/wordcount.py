
#!/usr/bin/python
file=open("words.txt","r+")
wordcount= {}   # this is a dictionary
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] = wordcount[word] + 1;
print(wordcount)
for theword,thewordcount in wordcount.items():  # wordcount is a dictionary
    # so you have theword as key and the wordcount as value 
    print(theword, thewordcount)
