

s = "abcdefghijklmnopqrs"

# Loop over some indexes.
for n in range(2, 4):
    # Print slices.
    print(n, s[n])
    print(n, s[n:n + 2])
    print(n, s[n:n + 3])
    print(n, s[n:n + 4:2])
    print(n, s[n:n + 6:2])
