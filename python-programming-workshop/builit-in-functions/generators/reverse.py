

class Reverse:
  def __init__(self, data):
    self.data = data
    self.index = len(data)
  def __iter__(self):
    return self
  def next(self):
    if self.index == 0:
      raise StopIteration()
    self.index = self.index - 1
    return self.data[self.index]

for mychar in Reverse('spam'):
  print(mychar)
