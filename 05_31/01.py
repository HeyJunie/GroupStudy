# 격자판 최대합

def solution(board):
    answer=float('-inf')
    n=len(board)
    sum1=0
    sum2=0
    for i in range(n):
        sum1=0
        sum2=0
        for j in range(n):
            sum1+=board[i][j]
            sum2+=board[j][i]
        answer=max(answer, sum1, sum2)
    sum1=0
    sum2=0
    for i in range(n):
        sum1+=board[i][i]
        sum2+=board[i][n-i-1]
    answer=max(answer, sum1, sum2)
    return answer

print(solution([[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27],
[19, 13, 30, 13, 19]]))