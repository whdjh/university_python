import math

a, b = map(int, input().split())

res1 = math.gcd(a, b)
res2 = math.lcm(a, b)

print(res1)
print(res2)