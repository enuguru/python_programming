
#Hold onto your hats boys, parse on a regular expression:

import re
mystring = 'zzzzzzabczzzzzzdefzzzzzzzzzghizzzzzzzzzzzz'
mylist = re.split("[a-m]+", mystring)
print(mylist)
#['zzzzzz', 'zzzzzz', 'zzzzzzzzz', 'zzzzzzzzzzzz']

#The regular expression "[a-m]+" means the lowercase letters a through m that occur one or more times 
#are matched as a delimiter. re is a library to be imported.
