#10은 2와 5로 구성
#2와 5 짝이 맞아야 10이 됨 2의 개수와 5의 개수중 더 작은게 10의 개수이다.
n, m = map(int, input().split())

def two_cnt(n):
    two = 0
    while n != 0:
        n //= 2
        two += n
    return two

def five_cnt(n):
    five = 0
    while n != 0:
        n //= 5
        five += n
    return five

res1 = two_cnt(n) - two_cnt(n - m) - two_cnt(m)
res2 = five_cnt(n) - five_cnt(n - m) - five_cnt(m)

print(min(res1, res2))