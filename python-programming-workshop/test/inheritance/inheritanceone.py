

class Animal(object):
  speakStr = 'Hello from Animal'
  pass
class Dog(Animal):
  pass

bark = Dog.speakStr
print(bark)
