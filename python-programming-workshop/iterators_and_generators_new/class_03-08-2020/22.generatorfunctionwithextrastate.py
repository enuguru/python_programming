
from collections import deque

class linehistory:

    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)
    def __iter__(self):
        for lineno, line in enumerate(self.lines,1):
            self.history.append((lineno, line))
            yield line
    def clear(self):
        self.history.clear()

#To use this class, you would treat it like a normal generator function. 
#However, since it creates an instance, you can access internal attributes, 
#such as the history attribute or the clear() method. For example:

with open('22.generatorfunctionwithextrastate.py') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
