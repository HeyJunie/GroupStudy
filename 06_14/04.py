# 동아리 개수

def solution(n, edges):
    cnt = 0
    ch = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for [a, b] in edges:
        graph[a].append(b)

    path = []

    def dfs(v):
        nonlocal cnt
        for nv in graph[v]:
            if ch[nv] == 0:
                path.append(nv)
                ch[nv] = 1
                dfs(nv)

    for i in range(1, n + 1):
        if ch[i] == 0:
            ch[i] = 1
            cnt += 1
            dfs(i)
    return cnt


print(solution(7, [[1, 2], [2, 3], [1, 4], [1, 5]]))