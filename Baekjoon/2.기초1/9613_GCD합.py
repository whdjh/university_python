#GCD(Greatest Common Divisor)란 최대공약수를 의미한다.
#테스트 케이스마다 주어진 수로 만들 수 있는 모든 쌍의 최대공약수를 구한 뒤, 이를 다 더한 것을 출력하면 된다.
#gcd구현
#def gcd(x, y):
#   if(y == 0):
#       return x
#   else:
#       return gcd(y, x % y)
import sys
import math

n = int(input())

for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    res = 0
    for j in range(1, len(arr)):
        for k in range(j + 1, len(arr)):
            res += math.gcd(arr[j], arr[k])
    print(res)