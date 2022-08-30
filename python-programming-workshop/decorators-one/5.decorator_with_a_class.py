
class decorator_class(object):

    def __init__(self, badri):
        print("I am the decorator_class.__init__(), and an instance of decorator class created")
        self._args = badri

    def __call__(self):
        print("I am the decorator_class.__call__(), and I am doing decoration job")
        self._args()

@decorator_class
def function_one():
    print("I am function one and I got decorated")

function_one()
