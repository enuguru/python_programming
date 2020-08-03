
# Compile this two-line program.
# ... <string> means it is a string, not a file.
# ... "exec" means multiple statements are present.
code = compile("""x += 1
print(x)""", "<string>", "exec")

# Execute compiled code with globals and locals.
x = 100
exec(code, globals(), locals())
