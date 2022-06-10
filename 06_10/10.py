# 조합 구하기

def solution(n, r):
    answer = []
    tmp = []
    def dfs(L, s):
        if L == r:
            answer.append(tmp.copy())
        else:
            for i in range(s, n+1):
                tmp.append(i)
                dfs(L+1, i+1)
                tmp.pop()
    dfs(0, 1)
    return answer

print(solution(4, 2))