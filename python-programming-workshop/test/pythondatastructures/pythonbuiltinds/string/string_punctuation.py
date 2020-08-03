
#Punctuation, whitespace. Let us look at two more occasionally-helpful constants in 
#the string module: punctuation and whitespace. These too can be looped over or tested.

#Tip: Instead of testing these strings with "in," consider using methods like isspace().

#Python that uses string.punctuation, whitespace

import string

# Display punctuation.
print(string.punctuation)

# The space is included in string.whitespace.
print(" " in string.whitespace)
print(string.whitespace)
