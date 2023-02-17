from itertools import permutations
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
pers = permutations(a)
result = 0

#최대, 최소// 다음최대, 다음최소// ->
for per in pers:
    ans = 0
    for i in range(len(per) - 1):
        ans += abs(per[i] - per[i + 1])
        
    if ans > result:
        result = ans
 
print(result)