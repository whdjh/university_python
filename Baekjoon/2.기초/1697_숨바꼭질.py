import sys
from collections import deque

def bfs(v):
    queue = deque([v])
    
    while queue:
        v = queue.popleft()
        if v == k:
            return dp[v]
        
        #기존 위치에서 이동하는 위치는 3가지 X - 1, X + 1, 2 x X 로 총 3가지가 있다. 즉 노드가 3개로 펼쳐져 나갈 수 있다.
        for next_v in (v - 1, v + 1, 2 * v):
            if 0 <= next_v < MAX and not dp[next_v]:
                dp[next_v] = dp[v] + 1
                queue.append(next_v)

MAX = 100001
n, k = map(int, sys.stdin.readline().split())
dp = [0] * MAX
print(bfs(n))