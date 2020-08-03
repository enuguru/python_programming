
# karthik the program is well done it works,
# my remark is, you need to check till half of the 
# string, that is till the condition i > j is satisfied
# is it not?  thereby some time can be saved


#palindrome check

# strA = "apple"
strA = "racecar"

lenA = len(strA)
i = 0
j = lenA - 1

while i < lenA and j >= 0:
    if strA[i] != strA[j]:
        break
    i+=1
    j-=1

if i == lenA:
    print(strA +" is palindrome")
else:
    print(strA + " is not a palindrome")

