import sys

notation = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int, sys.stdin.readline().split())
ans = ''

while n != 0:
    ans += str(notation[n % b])
    n //= b
    
print(ans[::-1])