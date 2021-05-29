
def my_function(country = "Norway"):
  print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def printinfo( name="Karthik", age = 35 ):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)


# Now you can call printinfo function
printinfo( age=50, name="Jatin" )
printinfo( name="Jatin" )
printinfo( age=30 )
printinfo( name="Jatin", age=50 )
printinfo()
