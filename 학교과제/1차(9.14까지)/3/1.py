A = {2, 4, 5}
B = {1, 2, 2, 1, 10, 4}
C = {3, 3, 3, 4}

res = A.intersection(B)

res2 = res.intersection(C)

res = A.union(B)

res = res.union(C)

ArBrCmA = res.difference(A)
