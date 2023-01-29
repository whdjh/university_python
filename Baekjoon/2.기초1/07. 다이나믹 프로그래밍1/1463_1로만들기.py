#다이나믹 프로그래밍의 개념은 큰 문제를 부분문제로 나누고, 이미 연산을 끝낸 값들에 대해선 그 값들을 재활용하는 것이다.
n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])