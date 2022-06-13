# 수열 추측하기

def solution(n, f):
    answer = []
    dy = [[0] * 35 for _ in range(35)]
    def combi(n, r):
        if dy[n][r] > 0:
            return dy[n][r]
        if n == r or r == 0:
            return 1
        else:
            dy[n][r] = combi(n-1, r-1) + combi(n-1, r)
            return dy[n][r]

    p = []
    b = []
    ch = [0] * (n+1)

    for i in range(n):
        b.append(combi(n-1, i))

    flag = 0
    def dfs(L, s):
        nonlocal answer, flag
        if flag == 1:
            return
        if L == n:
            if s == f:
                answer = p.copy()
                flag = 1
        else:
            for i in range(1, n+1):
                if ch[i] == 0:
                    ch[i] = 1
                    p.append(i)
                    dfs(L+1, s+(b[L]*p[-1]))
                    ch[i] = 0
                    p.pop()

    dfs(0, 0)
    return answer

print(solution(4, 16))
print(solution(5, 50))