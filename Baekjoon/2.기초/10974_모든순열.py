from itertools import combinations, permutations

n = int(input())
m = []

for i in range(n):
    m.append(i + 1)
    
per = permutations(m, n)		#순열

for p in per:
    print(*p)