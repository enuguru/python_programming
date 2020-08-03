
def yourfunction(): 
    global mystr
    print(mystr) 
    mystr = "I am fine"
    print(mystr) 

mystr = "Hello How are you doing?" 
print(mystr)
yourfunction()
print(mystr)
