
from random import randrange

NUM_RUNS = 10000
D_MAX = 6


def simulatingTwoDice():
    d1 = randrange(1,D_MAX+1)
    d2 = randrange(1,D_MAX+1)
    return (d1+d2)


expected = { 2 : 1/36, 3 : 2/36, 4 : 3/36, 5 : 4/36, \
             6 : 5/36, 7 : 6/36, 8 : 5/36, 9 : 4/36, \
             10 : 3/36, 11 : 2/36, 12 : 1/36 };

counts = { 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, \
           8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}             

for i in range(NUM_RUNS):
    t = simulatingTwoDice()
    counts[t] = counts[t] + 1

print("   Total    Simulated  Expected")
print("             Percent    Percent")
for i in sorted(counts.keys()):
    print("%5d   %11.2f   %8.2f" % \
          (i, counts[i] / NUM_RUNS * 100, expected[i] * 100))
