t = int(input())

def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))