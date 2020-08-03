
import time

def has_duplicates(values):
    # Same as above example.
    for i in range(0, len(values)):
        for x in range(i + 1, len(values)):
            if values[i] == values[x]:
                return True
    return False

# Contains no duplicates.
elements = [100, 200, 300, 400, 500, 600]
x=time.time();
print(x)
i = has_duplicates(elements)
y=time.time();
print(y)
time_elapsed=x-y
print(time_elapsed)
