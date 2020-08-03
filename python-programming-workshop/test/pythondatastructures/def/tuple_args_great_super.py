

#Tuple argument. A method in Python can receive any number of arguments stored in a 
#tuple. This requires the single-star syntax. A formal parameter of name *t can be 
#used as a tuple.

#Tip: The tuple in this program, of identifier t, can be used in the same way as any tuple.

#Python that receives tuple argument

def display(*t):
    # Print tuple.
    print(t)

    # Loop over tuple items.
    for item in t:
        print(item)

# Pass parameters.

display("San Francisco", "Los Angeles", "Sacramento")
display(2, 0, 1, 4)
