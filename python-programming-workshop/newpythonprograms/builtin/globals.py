
value1 = "cat"
value2 = "dog"

# Copy the globals dict so it does not change size.
g = dict(globals())

# Loop over pairs.
for item in g.items():
    print(item[0], "=", item[1])

