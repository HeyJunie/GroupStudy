# 부분 집합 구하기(DFS)

def solution(n):
    answer = []
    part = []
    def dfs(k):
        if k == n+1:
            if len(part):
                answer.append(part.copy())
        else:
            part.append(k)
            dfs(k+1)
            part.pop()
            dfs(k+1)
    dfs(1)
    return answer

solution(3)