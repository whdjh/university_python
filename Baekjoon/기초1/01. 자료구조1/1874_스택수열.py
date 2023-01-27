n = int(input())
stack = []
ans = []
flag = 0
cur = 1

for i in range(n):			#입력한 수를 만날때까지 반복하기
    num = int(input())
    while cur <= num:
        stack.append(cur)
        ans.append("+")
        cur += 1
    
    if stack[-1] == num:	#입력한 수를 맨위에서 만났다!
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in ans:
        print(i)