
# Program to count the number of each vowel in a string

# string of vowels
vowels = 'aeiou'

# take input from the user
ip_str = input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)
print(count)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)
