import sys

prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

#소수 체크, 소수아니면 1로 변환
for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2 * i, 1000001, i):
            check[j] = 1

t = int(sys.stdin.readline())

for i in range(t):
    cnt = 0
    n = int(sys.stdin.readline())
    for j in prime:
        if j >= n:
            break
        if not check[n - j] and j <= n - j:		#중복 카운트x
            cnt += 1
    print(cnt)