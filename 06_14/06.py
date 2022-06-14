# 토마토

from collections import deque


def solution(board):
    row = len(board)  # n
    col = len(board[0])  # m
    deq = deque()
    distance = [[0] * col for _ in range(row)]
    dx = [-1, 0, 1, 1]
    dy = [0, 1, 0, -1]
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                deq.append([i, j])

    while deq:
        cur = deq.popleft()
        for k in range(4):
            nx = cur[0] + dx[k]
            ny = cur[1] + dy[k]
            if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == 0:
                board[nx][ny] = 1
                distance[nx][ny] = distance[cur[0]][cur[1]] + 1
                answer = distance[nx][ny]
                deq.append([nx, ny])
    for i in range(row):
        for j in range(col):
            if board[i][j] == 0:
                return -1

    return answer


print(solution([[0, 0, -1, 0, 0, 0], [0, 0, 1, 0, -1, 0], [0, 0, -1, 0, 0, 0], [0, 0, 0, 0, -1, 1]]))