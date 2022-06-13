# 미로의 최단거리 통로

from collections import deque
def solution(board):
    dx = [-1, 0, 1, 1]
    dy = [0, 1, 0, -1]
    distance = [[0]*7 for _ in range(7)]
    deq = deque()
    deq.append((0, 0))
    board[0][0] = 1
    print(deq)
    while deq:
        loc = deq.popleft()
        for k in range(4):
            x = loc[0] + dx[k]
            y = loc[1] + dy[k]
            if x >=0  and x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
                board[x][y] = 1
                distance[x][y] = distance[loc[0]][loc[1]] + 1
                deq.append((x, y))
    if distance[6][6] == 0:
        return -1
    else:
        return distance[6][6]


print(solution([[0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [1, 1, 0, 1, 0, 1, 1],
                [1, 1, 0, 1, 0, 0, 0],
                [1, 0, 0, 0, 1, 0, 0],
                [1, 0, 1, 0, 0, 0, 0]]))