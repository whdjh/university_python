from collections import deque

# n=정점개수, m=간선개수, v=탐색시작점
n, m, v = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    a,b = map(int, input().split())
    dp[a][b] = dp[b][a] = 1

def dfs(v):
    visited[v] = 1
    print(v,end=' ')
    for i in range(1, n + 1):
        if(visited[i] == 0 and dp[v][i] == 1):
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = 0		#반대로 생각해서 0이면 방문했다고 보면 됨
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if(visited[i] == 1 and dp[v][i] == 1):
                queue.append(i)
                visited[i] = 0

dfs(v)
print()
bfs(v)