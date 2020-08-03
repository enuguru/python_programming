

from array import array

# Create an empty int array.
a = array("i")

# Append ten million ints.
for i in range(0, 100):
    a.append(i)

# Finished.
print("DONE")
input()
