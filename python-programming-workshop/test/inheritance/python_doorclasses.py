
class Door:
    def __init__(self):
        self.status = "closed"

    def open(self):
        self.status = "open"

    def close(self):
        self.status = "closed"

    def is_open(self):
        return self.status == "open"


class BooleanDoor:
    def __init__(self):
        self.status = True

    def open(self):
        self.status = True

    def close(self):
        self.status = False

    def is_open(self):
        return self.status


door = Door()
bool_door = BooleanDoor()

door.close()
a=door.is_open()
print(a)

bool_door.open()
a=bool_door.is_open()
print(a)

bool_door.close()
a=bool_door.is_open()
print(a)
