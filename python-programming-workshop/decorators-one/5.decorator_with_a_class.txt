
# PythonDecorators/my_decorator.py
class my_decorator(object):

    def __init__(self, badri):
        print("inside my_decorator.__init__()")
        badri() # Prove that function definition has completed

    def __call__(self):
        print("inside my_decorator.__call__()")

@my_decorator
def aFunction():
    print("inside aFunction()")

aFunction()
print("Finished decorating aFunction()")
