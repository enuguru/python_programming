
# there is no function overaloding in python
# if you need two differenct behaviour, then
# give default values

class A:
    def stackoverflow(self, i='20'):    
        print('only method')

ob=A()
ob.stackoverflow(2)
ob.stackoverflow()
