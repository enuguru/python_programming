
vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled

one = [x*2 for x in vec]
print(one)

# filter the list to exclude negative numbers
two = [x for x in vec if x >= 0]
print(two)

# apply a function to all the elements
three = [abs(x) for x in vec]
print(three)

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruitnew = [weapon.strip() for weapon in freshfruit]
print(freshfruitnew)

# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
# the tuple must be parenthesized, otherwise an error is raised
four = [(x, x**2) for x in range(6)]
print(four)

#SyntaxError: invalid syntax
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
five = [num for elem in vec for num in elem]
print(five)

