import sys

nge = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
ans = [-1] * nge

for i in range(nge):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    stack.append(i)
print(*ans)        #파이썬에서 배열을 출력할 때, *붙이면 공백을 기준으로 원소들만 나열