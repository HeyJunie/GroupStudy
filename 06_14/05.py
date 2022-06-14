# 섬나라 아일랜드(DFS)

def solution(board):
    n = len(board)
    cnt = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    graph = [[0] for _ in range(n+1)]

    def dfs(x, y):
        nonlocal n
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                board[nx][ny] = 0
                dfs(nx, ny)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt += 1
                board[i][j] = 0
                dfs(i, j)

    return cnt


print(solution([[1, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1],
                [1, 1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0]]))