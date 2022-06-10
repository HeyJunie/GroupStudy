# 조합의 경우수(Memorization)

def solution(n, r):
    dy = [[0] * 35 for _ in range(35)] # 메모리제이션을 위한
    def dfs(n, r):
        if dy[n][r] > 0:
            return dy[n][r]
        if n == r or r == 0:
            return 1
        else:
            dy[n][r] = dfs(n-1, r-1) + dfs(n-1, r)
            return dy[n][r]
    return dfs(n, r)

print(solution(5, 3))
print(solution(33, 19))