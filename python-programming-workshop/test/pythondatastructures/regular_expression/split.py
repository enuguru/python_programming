

#Split. 

#The re.split() method accepts a pattern argument. This pattern specifies the 
#delimiter. With it, we can use any text that matches a pattern as the delimiter 
#to separate text data.

#Here:We split the string on one or more non-digit characters. The regular expression 
#is described after the script output.

#Tip:A split() method is also available directly on a string. This method handles no 
#regular expressions. It is simpler.


#Python program that uses split

import re

# Input string.  see this is a string if we use "double quotes" in a word or sentence
value = "one 1 two 2 three 3"

# Separate on one or more non-digit characters.
result = re.split("\D+", value)

# Print results.
for element in result:
    print(element)

#Pattern details

#Pattern: \D+

#  \D+      One or more non-digit characters.
