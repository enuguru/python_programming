
class Foo:
  def __call__(self):
    print('called')

foo_instance = Foo()
foo_instance() #this is calling the __call__ method
