


value = "abcdefgh"
pairs = []

# Loop over string.
# ... Use step of 2 in range built-in.
# ... Extract pairs of letters into a list of tuples.
for i in range(1, len(value), 2):
    one = value[i - 1]
    two = value[i]
    pairs.append((one, two))

# Display list of tuple pairs.
for pair in pairs:
    print(pair)
