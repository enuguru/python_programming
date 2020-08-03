
#Python program that creates a namedtuple

import collections

# Specify the Employee namedtuple.
Employee = collections.namedtuple("Employee", ["id", "title", "salary"])

# Create Employee instance.
e = Employee(1, "engineer", 10000)

# Display Employee.
print(e)
print("Title is", e.title)
