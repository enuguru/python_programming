
students = {}

# Add three key-value tuples to the dictionary.
students["Vaishnavi"] = [2,4]
students["Jothi"] = [1,34]
students["Karthik"] = [4,56]
students["Jayashree"] = [20.3,4.5]
students["Raju"] = [20,4]
students["Lakshman"] = [50.3,4.5]
students["Raman"] = [20.3,1.5]
students["John"] = [20.3,3.5]
students["Godspeed"] = [2.3,4]
students["Angelina"] = [20.3,45]
students["Kumar"] = [20.3,4.5]
students["Kirthika"] = [20.3,4.5]
students["Ranjith"] = [20.3,4.5]
students["Maravan"] = [20.3,4.5]
students["Sanjeev"] = [20.3,4.5]
students["Devasagayam"] = [20.3,4.5]

# Get syntax 1.
print(students["Vaishnavi"])

# Get syntax 2.
print(students.get("Raghu"))
print(students.get("Raghu", "Raghu not found"))
print(students.get('Vaishnavi'))
print(sorted(students))
print(students["Raju"][1])
#print(students)
