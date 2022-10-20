p = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            p += i + j + k
#O(n^3)