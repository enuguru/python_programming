
dic = {"key 1":"value 1","key b":"value b"}

#print the keys:
for key in dic.iterkeys():
    print key

#print the values:
for value in dic.itervalues():
    print value

#print key and values
for key, value in dic.iteritems():
    print key, value
