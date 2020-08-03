

#Python that optimizes if-checks

values = [[1, 1], [2, 1], [1, 1], [3, 1]]

for pair in values:
    # We test the first part of each list first.
    # ... It is most specific.
    # ... This reduces total checks.
    if pair[0] == 1 and pair[1] == 1:
        print(True)
