t = int(input())
ans = [1, 2, 4]

for i in range(3, 10):
    ans.append(ans[i - 3] + ans[i - 2] + ans[i - 1])
    
for i in range(t):
    n = int(input())
    print(ans[n - 1])