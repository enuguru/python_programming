

string = input("Enter a string:  ")

is_palindrome = True

for i in range(0,len(string) // 2):
    if string[i] != string[len(string) - i - 1]:
        is_palindrome = False

if is_palindrome:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
