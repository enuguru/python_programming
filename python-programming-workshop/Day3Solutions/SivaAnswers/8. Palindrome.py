
# nice siva no issues
# however your logic goes till the 
# end of the string right?
# can you traverse only till half way through
# the string?

def is_palindrome(string):
    string = string.lower()
    is_palindrome = True
    for i,c in enumerate(string):
        if string[i] != string[-(i+1)]:
            is_palindrome = False
            break
    print(is_palindrome)


is_palindrome("MADAm")
