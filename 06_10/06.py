# 중복순열 구하기

def solution(n, m):
    answer = []
    tmp = []
    def dfs(L):
        if L == m:
            answer.append(tmp.copy())
        else:
            for i in range(1, n+1):
                tmp.append(i)
                dfs(L+1)
                tmp.pop()
    dfs(0)
    return answer
print(solution(3, 2))