
with open("words.txt") as openfile:
    for line in openfile:
        m = re.search(r'(color\=.+?(?= )|color\=.+?$)', line)
	   if m:
              text = m.group() # Matched text here
              print(text)
