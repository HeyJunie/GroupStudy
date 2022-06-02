# 회장선거

def solution(n, votes, k):
    answer = []
    report = [[0]*n for _ in range(n)]
    candidate = [0]*n
    for x, y in votes:
        report[x][y] = 1
    for i in range(n):
        cnt = 0
        for j in range(n):
            if report[j][i] == 1:
                cnt += 1
        if cnt >= k:
            candidate[i] = 1
    print(candidate)
    for i in range(n):
        cnt = 0
        for j in range(n):
            if report[i][j] == 1 and candidate[j] == 1:
                cnt += 1
        answer.append(cnt)

    return answer

print(solution(4, [[0, 1], [0, 3], [1, 2], [2, 0], [2, 3], [3, 0]], 2))