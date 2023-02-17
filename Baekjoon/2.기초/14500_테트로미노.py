import sys

# 상, 하, 좌, 우
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = 0

# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
def dfs(x, y, dsum, cnt):
    global result
    # 모양 완성되었을 때 최대값 계산
    if cnt == 4:
        result = max(result, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for i in range(4):
        ix = x + move[i][0]
        iy = y + move[i][1]
        if 0 <= ix < n and 0 <= iy < m and not visited[ix][iy]:
            # 방문 표시 및 제거
            visited[ix][iy] = True
            dfs(ix, iy, dsum + board[ix][iy], cnt + 1)
            visited[ix][iy] = False

# ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산
def exce(x, y):
    global result
    for i in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = board[x][y]
        for j in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (i + j) % 4
            ix = x + move[t][0]
            iy = y + move[t][1]

            if not (0 <= ix < n and 0 <= iy < m):
                tmp = 0
                break
            tmp += board[ix][iy]
        # 최대값 계산
        result = max(result, tmp)

for i in range(n):
    for j in range(m):
        # 시작점 visited 표시
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
        exce(i, j)

print(result)