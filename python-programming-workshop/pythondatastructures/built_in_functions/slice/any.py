

# Test any with all zero elements.
# ... These evaluate to false.
values = [0, 0, 0]
result = any(values)
print("ANY", values, result)

# Test any with a 1 element.
# ... This element evaluates to true, so any is true.
values = [0, 0, 1]
result = any(values)
print("ANY", values, result)
