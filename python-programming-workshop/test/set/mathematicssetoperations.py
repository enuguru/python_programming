

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("This gives the elements of A",A)
print("This gives the elements of B",B)

print("This give the union of A B that is A | B", A | B)

print("This gives the union of A B that is A.union(B)",A.union(B))
print("This gives the union of B A that is B union(A)",B.union(A))

print("This is A intersection B", A & B)


print("This gives the intersection of A with B A.intersection(B)",A.intersection(B))
print("This gives the intersection of B with A B.intersection(A)",B.intersection(A))

print("This gives elements in A and not in B A-B",A-B)
print("This gives elements in B and not in A B-A",B-A)

print("This gives elements in A and not in B A.difference(B)",A.difference(B)) 
print("This gives elements in B and not in A B.difference(A)",B.difference(A)) 
