#Sets exercises

# create 3 sets
A = {1,2,3,4,5,7}
B = {2,4,5,9,12,24}
C = {2,4,8}

print(A)
print(B)
print(C)

# Iterate all elements in C and add them to A and B
for n in C:
    A.add(n)
    B.add(n)

print("A after adding elements: ", A)
print("B after adding elements: ", B)

print("Intersection of A and B: ", A.intersection(B))
print("The union of A and B: ", A.union(B))
print("Elements in A but not in B: ", A.difference(B))
print("The length of A: ", len(A))
print("The length of B: ", len(B))
print("The maximum value of A union B: ", max(A.union(B)))
print("The minimum value of A union B: ", min(A.union(B)))