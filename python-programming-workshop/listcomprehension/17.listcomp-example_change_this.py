
text = "hello how are you doing 
i am doing fine, I hope you 
are doing fine too"

# Without list comprehension
list_of_words = []
for sentence in text:
    for word in sentence:
       list_of_words.append(word)
print(list_of_words)
