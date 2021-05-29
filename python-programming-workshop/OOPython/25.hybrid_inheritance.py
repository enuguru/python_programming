
class GrandPa:
    def __init__(self):
        print("Grand Pa")

class Mother(GrandPa):
    def __init__(self):
        #print('f', super())
        #super().__init__()
        print("This is mother")

class Father(GrandPa):
    def __init__(self):
        #print('m', super())
        #super().__init__()
        print("father")

class child(Father,Mother):
    def __init__(self):
        print('This is child')
        super().__init__()
        #super().__init__()

c = child()
