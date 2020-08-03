

# Python program that tests starts, ends

import re

list = ["123", "4cat", "dog5", "6mouse"]
for element in list:

    # See if string starts in digit.
    m = re.match("^\d", element)
    if m:
        print("START:", element)

    # See if string ends in digit.
    m = re.match(".*\d$", element)
    if m:
        print("  END:", element)


# Pattern details

# ^\d     Match at the start, check for single digit.
# .*\d$   Check for zero or more of any char.
#         Check for single digit.
#         Match at the end.
