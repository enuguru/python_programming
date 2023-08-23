
class decorator_class:

    def __init__(self):
        print("I am the decorator_class.__init__(), and an instance of decorator class created")

    def __call__(self):
        print("I am the decorator_class.__call__(), and I am doing decoration job")

x = decorator_class()
x()
