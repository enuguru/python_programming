
from collections import defaultdict

#!/usr/bin/python
file=open("words.txt","r+")
wordcount= defaultdict(lambda:0)   # this is a dictionary
for word in file.read().split():
        wordcount[word] = wordcount[word] + 1;
print(wordcount)
for theword,thewordcount in wordcount.items():  # wordcount is a dictionary
                                                # so you have theword as key and the wordcount as value 
    print(theword, thewordcount)
