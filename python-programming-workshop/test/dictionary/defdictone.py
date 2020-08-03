

L = ['apple','red','apple','red','red','pear']
from collections import defaultdict
d = defaultdict(int)
for i in L:
   d[i] += 1
print(d)
