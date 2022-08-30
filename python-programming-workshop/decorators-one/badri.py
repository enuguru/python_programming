
def firstfunction(parameter):
      print('My name is Badri')
      return parameter

def secondfunction(parameter):
      print('I Study Computer Science and Engineering')
      return parameter

def thirdfunction(parameter):
      print('Karthik is playing Counter-Strike')
      return parameter

@secondfunction
@firstfunction
@thirdfunction
def func1():
     print('This is Python3')
     return

func1()
