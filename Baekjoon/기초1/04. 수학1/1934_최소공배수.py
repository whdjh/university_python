import math

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    res = math.lcm(a, b)
    print(res)