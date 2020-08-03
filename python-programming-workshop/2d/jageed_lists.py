
#Jagged lists. The term "jagged" implies that sub lists have uneven lengths. 
#Here we create a list of two lists—one of length 2, the other of length 5. 
#We display their lengths.

#Python program that uses jagged lists

# A jagged list.
values = [[10, 20], [30, 40, 50, 60, 70]]

for value in values:
    # Print each row's length and its elements.
    print(len(value), value)

#Output

#2 [10, 20]
#5 [30, 40, 50, 60, 70]
