

A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

result = A.difference_update(B)            


print('A = ', A)                result will be None
print('B = ', B)                A will be equal to A-B
print('result = ', result)      B will be unchanged
