

class Funky:
    def __init__(self, y):
        print("See I am getting initialized")
    def __call__(self):
        print("Look at me, I work like a function!!")

x = 20
f = Funky(x)
#f()
