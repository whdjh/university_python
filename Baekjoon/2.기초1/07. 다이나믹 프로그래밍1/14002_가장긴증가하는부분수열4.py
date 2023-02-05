n = int(input())
a = list(map(int, input().split()))

dp = [1] * (n + 1)

for i in range(len(a)):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

x = max(dp)

result = []

for i in range(n - 1, -1, -1):
    if dp[i] == x:
        result.append(a[i])
        x -= 1
        
result.reverse()

for i in result:
    print(i, end=' ')