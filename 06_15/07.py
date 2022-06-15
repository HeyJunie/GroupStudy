# 스도쿠(DFS 활용)

import collections, heapq


def solution(board):
    answer = []
    p = []
    chRow = [[0] * 10 for _ in range(9)]
    chCol = [[0] * 10 for _ in range(9)]
    chGroup = [[0] * 10 for _ in range(9)]

    def find(x, y):
        return (x // 3) * 3 + (y // 3)

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                p.append([i, j])
            else:
                chRow[i][board[i][j]] = 1
                chCol[j][board[i][j]] = 1
                chGroup[find(i, j)][board[i][j]] = 1
    flag = 0
    n = len(p)

    def dfs(L):
        nonlocal flag
        if flag == 1:
            return
        if L == n:
            for x in board:
                answer.append(x.copy())
            flag = 1
        else:
            xx = p[L][0]
            yy = p[L][1]
            gg = find(xx, yy)
            for i in range(1, 10):
                if chRow[xx][i] == 0 and chCol[yy][i] == 0 and chGroup[gg][i] == 0:
                    chRow[xx][i] = chCol[yy][i] = chGroup[gg][i] = 1
                    board[xx][yy] = i
                    dfs(L + 1)
                    chRow[xx][i] = chCol[yy][i] = chGroup[gg][i] = 0
                    board[xx][yy] = 0

    dfs(0)
    return answer


print(solution([[0, 2, 3, 0, 5, 0, 7, 8, 9], [0, 5, 6, 0, 8, 9, 1, 0, 3], [0, 8, 9, 1, 0, 3, 0, 5, 6], [0,
                                                                                                        1, 0, 0, 6, 0,
                                                                                                        8, 9, 0],
                [3, 0, 5, 0, 9, 7, 0, 1, 4], [0, 9, 7, 0, 1, 0, 0, 6, 5], [5, 3, 0,
                                                                           6, 0, 2, 9, 7, 8],
                [6, 0, 2, 9, 0, 8, 5, 3, 1], [9, 0, 8, 0, 3, 0, 6, 0, 2]]))