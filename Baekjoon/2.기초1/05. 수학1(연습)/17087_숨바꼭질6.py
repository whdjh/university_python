#문제에서 구하고자 하는 것은 수빈이와 동생들의 거리 차들의 최대공약수
import math
        
n, s = map(int, input().split())
a = list(map(int, input().split()))
res = abs(s - a[0])	#절대값함수

if s == 1:
    print(res)
else:
    for i in range(1, n):
        res = math.gcd(res, abs(s - a[i]))
    print(res)