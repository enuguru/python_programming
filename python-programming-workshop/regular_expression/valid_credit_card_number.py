

# check if the given credit card number is valid
# do not give any space between regular expression, it will give error

#the total numbers are 16
#there can be - after 4 numbers
#the number should start with 4,5,6
#there should not be ' ','_'
#no same character should repeat 4 times

#4344-4456-8734-5677
import re
s = input()
if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$",s) and not re.search(r"([\d])\1\1\1",s.replace("-","")):
    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$",s) and not re.search(r"([\d])\1\1\1",s.replace("-","")):
        print("The credit card is valid")
else:
    print("The credit card is not valid")
