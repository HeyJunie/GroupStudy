# 경로 탐색(인접 리스트)

def solution(n, edges):
    cnt = 0
    ch = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for [a, b] in edges:
        graph[a].append(b)

    path = []

    def dfs(v):
        nonlocal cnt
        if v == n:
            cnt += 1
            print(path)
        else:
            for nv in graph[v]:
                if ch[nv] == 0:
                    path.append(nv)
                    ch[nv] = 1
                    dfs(nv)
                    path.pop()
                    ch[nv] = 0

    path.append(1)
    ch[1] = 1
    dfs(1)
    return cnt


print(solution(5, [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 5], [3, 4], [4, 2], [4, 5]]))