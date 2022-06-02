# 숫자 충돌

def solution(board):
    while True:
        crush = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if j > 1 and board[i][j] and board[i][j] == board[i][j-1] == board[i][j-2]:
                    crush = crush | {(i, j), (i, j-1), (i, j-2)}
                if i > 1 and board[i][j] and board[i][j] == board[i-1][j] == board[i-2][j]:
                    crush = crush | {(i, j), (i-1, j), (i-2, j)}

        if not crush:
            break
        for i, j in crush:
            board[i][j] = 0

        for j in range(len(board[0])):
            idx = len(board)-1
            for i in reversed(range(len(board))):
                if board[i][j]:
                    board[i][j], board[idx][j] = board[idx][j], board[i][j]
                    # board[idx][j] = board[i][j]
                    idx -= 1
            # for i in range(idx + 1):
            #     board[i][j] = 0
    return board

print(solution([[5, 5, 3, 7, 5], [6, 2, 2, 9, 5], [7, 2, 2, 7, 8], [3, 3, 2, 3, 5], [5, 8, 5, 5, 3]]))
print(solution(
    [[5, 5, 3, 7, 5, 23, 11], [6, 2, 2, 9, 5, 23,11], [7, 2, 2, 7, 8, 23, 11],
     [3, 3, 2, 3, 5, 23, 11], [5, 8, 5, 5, 3, 23, 11]]
))