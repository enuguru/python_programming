
# karthick the program works fine no issues
# can you try this without using regular expression?
# possible? since RE is a heavy module

#good password check
#8 characters long, 1 uppercase, 1 lowercase, 1 numeric, 1 special

import re

passwordA = "Appple$11"
# passwordA = "apple"

# print(len(passwordA) < 8)
# print(re.search(r"\d", passwordA) is None)
# print(re.search(r"[A-Z]", passwordA) is None)
# print(re.search(r"[a-z]", passwordA) is None)
# print(re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', passwordA) is None)

if len(passwordA) < 8 or (re.search(r"\d", passwordA) is None) or (re.search(r"[A-Z]", passwordA) is None) or (re.search(r"[a-z]", passwordA) is None) or (re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', passwordA) is None):
    print("invalid password")
else:
    print("valid password")
