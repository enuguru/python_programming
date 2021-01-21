
import re

# r'^[+-]?[0-9]*\.[0-9]+$'

for _ in range(int(input())):
    print(bool(re.match(r'^[+-]?[0-9]*\.[0-9]+$',input())))

