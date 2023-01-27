from collections import deque

n, k = map(int, input().split())	#map(적용할 함수, 반복 가능한 자료형)
queue = deque(range(1, n + 1))
ans = []
 
while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())
 
print(str(ans).replace('[', '<').replace(']', '>'))