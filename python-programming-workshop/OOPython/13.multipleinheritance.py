
class First(object):
    def __init__(self):
        print("first")

class Second(First):
    def __init__(self):
        print("second")

class Third(First):
    def __init__(self):
        print("third")

class Fourth(Third, Second):
    def __init__(self):
        super(Fourth, self).__init__()
        print("that's it")

a = Fourth();
