
class GrandPa:
    def __init__(self):
        self.x = 25
        print("Grand Pa")

class Father(GrandPa):
    def __init__(self):
        #GrandPa.__init__(self)
        print("This is father")
        print(self.x)

class Mother(GrandPa):
    def __init__(self):
        print("mother")
        print("Mother")

c = Father()
