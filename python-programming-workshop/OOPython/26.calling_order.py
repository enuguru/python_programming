
class GrandPa:
    def __init__(self):
        print("Grand Pa")

class Father(GrandPa):
    def __init__(self):
        print("This is father")

class Mother(GrandPa):
    def __init__(self):
        print("mother")
        print("Mother")

c = Father()
