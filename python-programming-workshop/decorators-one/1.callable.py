

class Foo:

  def __init__(self):
      print("Now constructor is getting called")

  def __call__(self):  # dunder method or magic method
    print('This is the print statement in the __call__ function which is called')

foo_instance = Foo()
print(foo_instance)
foo_instance() #this is calling the __call__ method


Foo()()


def newfunc():
    print("This is new function")

#newfunc()
