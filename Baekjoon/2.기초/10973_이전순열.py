n = int(input())
next_p = list(map(int, input().split()))
flag = 0

for i in range(n - 1, 0, -1):
    if next_p[i - 1] > next_p[i]:  #뒷 값 < 앞 값
        for j in range(n - 1, 0, -1):
            if next_p[i - 1] > next_p[j]:
                next_p[i - 1], next_p[j] = next_p[j], next_p[i - 1]
                next_p = next_p[:i] + sorted(next_p[i:], reverse = True)
                flag = 1
                break
            
    if flag == 1:
        print(*next_p)
        break
    
if flag == 0:
    print(-1)