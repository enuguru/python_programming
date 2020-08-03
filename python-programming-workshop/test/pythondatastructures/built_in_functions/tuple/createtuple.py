
#Tuple. A tuple stores values. It is similar to a list but uses different syntax. With tuples we cannot 
#change elements. This makes programs more predictable.

#Values. Tuples can be used as values:

#unlike classes, they never change. Often we need to hold values together. Suppose an element has a 
#shape and a color. This forms a tuple pair.


#Create. We first revisit the concept of immutability. A tuple cannot be changed after created. 
#So the creation syntax is important. We use parentheses "(" and ")" to create tuples.

#Zero elements:To create a tuple with zero elements, use only the two parentheses "()".

#One element:For a tuple with one element, use a trailing comma. This helps Python tell that 
#you don't mean an expression, such as (1 + 2).

#Two elements:For a tuple with two or more elements, use a comma between elements. 
#No ending comma is needed.


# Zero-element tuple.
a = ()
# One-element tuple.
b = ("one",)
# Two-element tuple.
c = ("one", "two")

print(a)
print(len(a))

print(b)
print(len(b))

print(c)
print(len(c))
