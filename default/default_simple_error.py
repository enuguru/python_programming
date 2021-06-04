def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Hrishikesh")
greet("Shalini", "How do you do?")

def greet(msg = "Good morning!", name):
#greet(name = "Bruce",msg = "How do you do?")

# 2 keyword arguments (out of order)
#greet(msg = "How do you do?",name = "Bruce") 

#1 positional, 1 keyword argument
#greet("Bruce", msg = "How do you do?")
