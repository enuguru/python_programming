
## python program to find whether the given words are anagrams of each other ##

# find if two strings are anagrams of each other and
# report the answer as "yes" or "no"


first_string = input(" Give first string : ")
second_string = input(" Give second string : ")

first_string = sorted(first_string)
second_string = sorted(second_string)

if(first_string == second_string):
    print(" Yes They are anagrams. ")
else:
    print(" No They are not anagrams. ")
