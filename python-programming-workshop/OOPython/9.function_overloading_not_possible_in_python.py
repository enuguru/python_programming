
# there is no function overaloding in python
# if you need two differenct behaviour, then
# give default values

class thisclass:
    def goodone(self, i='20'):    
        print('only method')
        print(i)

ob=thisclass()
ob.goodone(2)
ob.goodone()
