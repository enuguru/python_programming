
class Shape:
    # class or static variable
    cat = 'Geometrical'
    
    def __init__(self, type):
        # instance variable
        self.typ = type
    
    # method to show data
    def show(self):
        # accessing class variable
        print('Shape is of category: ', Shape.cat)
        # accessing instance variable
        #print('And shape is: ', self.type)


tr = Shape('Triangle')
sq = Shape('Square')
rec = Shape('Circle')

tr.show()
sq.show()
rec.show()
