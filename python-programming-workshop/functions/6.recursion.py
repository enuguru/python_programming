

#In recursion, a method calls itself. This helps solve complex problems. This next 
#program solves no problems. Instead it demonstrates recursion. It ceases once 
#its argument exceeds 10.

#Note: With recursion, we solve search problems. For example, we can determine all 
#possible ways to count change.

#Note 2: If a recursive method calls itself in only one spot, it can be rewritten 
#to instead use iteration like While or For

#Python program that uses recursion

def recursive(depth):
    # Stop recursion if depth exceeds 10.
    if depth > 10:
        return
    print(depth)
    # Call itself.
    recursive(depth + 1)

# Begin.
recursive(7)
