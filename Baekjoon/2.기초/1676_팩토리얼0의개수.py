n = int(input())
cnt = 0

#n이 5로 나누어 떨어지는 수가 몇개인지 파악하면 0의 개수를 알 수 있다
while n != 0:
    n //= 5
    cnt += n
        
print(cnt)