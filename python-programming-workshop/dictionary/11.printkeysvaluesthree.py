
# highlighting how to use a named variable within a string:
dict = {'a': 1, 'b': 2}

# simple method:
print "a %(a)s" % dict
print "b %(b)s" % dict

# yields:
# a 1
# b 1


# programmatic method:
for key in dict:
    val = '%('+key+')s'
    print key, val % dict

# yields:
# a 1
# b 1

# using list comprehension
print "\n".join(["%s: %s" % (key, ('%('+key+')s') % dict) for key in dict])

# yields:
# a: 1
# b: 1
