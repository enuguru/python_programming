
class Animal(object):
  speakStr = 'Hello from Animal'
  pass

class Dog(Animal):
  speakStr = 'Hello from Dog'
  pass

bark = Dog.speakStr;
print(bark)
