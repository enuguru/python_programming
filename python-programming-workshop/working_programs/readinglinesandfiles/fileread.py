
#!/usr/bin/python

# Open a file
fo = open("filewrite.txt", "r+")
str = fo.read(50);
print "Read String is : ", str
# Close opend file
fo.close()
