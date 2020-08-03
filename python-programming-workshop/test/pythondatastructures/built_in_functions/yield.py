

#Yield

#We introduce the yield keyword. The term yield has a meaning similar to 
#"produce": it dispatches specified elements. Unlike return, control returns 
#again to the method. Here, the odds() method yields odd elements in an iterable.

#Yield-keyword

#Info:The yield statement can return an expression, not just a variable. Try 
#changing "yield a" to "yield a + 1".

#Also:The yield pattern here is the more powerful form. It can filter and transform elements.

#Python program that uses yield

def odds(arg):
    # Yield odd elements in the iterable.
    for a in arg:
        if a % 2 != 0:
            yield a

# An input list.
items = [100, 101, 102, 103, 104, 105]

# Display all odd items.
for item in odds(items):
    print(item)

# Print copied list. you convert it to list and then print
copy = list(odds(items))
print(copy)
