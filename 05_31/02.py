# 봉우리

def solution(board):
    n = len(board)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    board.insert(0, [0]*n)
    board.append([0]*n)
    for x in board:
        x.insert(0, 0)
        x.append(0)
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if any(board[i][j] <= board[i + dx[k]][j + dy[k]] for k in range(4)):
                continue
            cnt += 1
    return cnt

print(solution([[5, 3, 7, 2, 3], [3, 7, 1, 6, 1], [7, 2, 5, 3, 4], [4, 3, 6, 4, 1], [8, 7, 3, 5, 2]]))