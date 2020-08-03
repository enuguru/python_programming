
#Python program that uses default arguments

def computesize(width=10, height=2):
    return width * height

print(computesize()) # 10, 2: defaults used.
print(computesize(5)) # 5, 2: default height.
print(computesize(height=3)) # 10, 3: default width.
