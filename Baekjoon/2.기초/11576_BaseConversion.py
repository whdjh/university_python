import math

a, b = map(int, input().split())
n = int(input())
lists = list(map(int, input().split()))
ten = 0		#10진법
res = []
ans = ''

for i in range(n):
    ten += int(lists[i] * math.pow(a, n - i - 1))

while ten:
    num = ten % b
    res.append(str(num))
    ten = ten // b

res = res[::-1]
ans = ' '.join(res)

print(ans)