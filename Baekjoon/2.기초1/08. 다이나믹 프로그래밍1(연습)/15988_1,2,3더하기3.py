t = int(input())
n = []

for i in range(t):
    n.append(int(input()))
    
maxN = max(n)

dp = [0 for _ in range(1000001)]
dp[0], dp[1], dp[2] = 1, 1, 2

for i in range(3, 1000001):
    dp[i] = (dp[i - 3] % 1000000009 + dp[i - 2] % 1000000009 + dp[i - 1] % 1000000009)
    
for i in n:
    print(dp[i] % 1000000009)