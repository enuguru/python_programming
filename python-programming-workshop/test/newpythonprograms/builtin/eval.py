
# Expression is first argument.
# ... Global dict is second argument.
# ... Local dict is third argument.
result = eval("i ** 2", None, {"i": 3})

# Three squared is 9.
print(result)
