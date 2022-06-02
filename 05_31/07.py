# 스토쿠 검사

def solution(board):
    answer = "YES"
    n = len(board)
    for i in range(n):
        width = set() # 중복이 아닌것을 찾아야 함
        height = set()
        for j in range(n):
            width.add(board[i][j])
            height.add(board[j][i])
            if len(width) != 9 or len(height) != 9:
                return "NO"

    for i in range(3):
        for j in range(3):
            by = set()
            for k in range(3):
                for l in range(3):
                    by.add(board[i*3+k][j*3+l])
            if len(by) != 9:
                return "NO"
    return answer

print(solution([
[2, 4, 3, 6, 2, 8, 5, 7, 8],
[4, 7, 2, 1, 3, 9, 4, 6, 9],
[9, 8, 6, 7, 5, 4, 2, 3, 1],
[3, 9, 1, 5, 4, 2, 7, 8, 6],
[4, 6, 8, 9, 1, 7, 3, 5, 2],
[7, 2, 5, 8, 6, 3, 9, 1, 4],
[2, 3, 7, 4, 8, 1, 6, 9, 5],
[6, 1, 9, 2, 7, 5, 8, 4, 3],
[8, 5, 4, 3, 9, 6, 1, 2, 7]])) #NO

print(solution([
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 1, 4, 3, 6, 5, 8, 9, 7],
    [3, 6, 5, 8, 9, 7, 2, 1, 4],
    [8, 9, 7, 2, 1, 4, 3, 6, 5],
    [5, 3, 1, 6, 4, 2, 9, 7, 8],
    [6, 4, 2, 9, 7, 8, 5, 3, 1],
    [9, 7, 8, 5, 3, 1, 6, 4, 2]])) #YES