# 경로 탐색 (인접 행렬)

def solution(n, edges):
    ch = [0] * (n + 1)
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    cnt = 0
    for [a, b] in edges:
        graph[a][b] = 1

    path = []

    def dfs(v):
        nonlocal cnt
        if v == n:
            cnt += 1
            print(path)
        else:
            for i in range(1, n + 1):
                if graph[v][i] == 1 and ch[i] == 0:
                    path.append(i)
                    ch[i] = 1
                    dfs(i)
                    path.pop()
                    ch[i] = 0

    path.append(1)
    ch[1] = 1
    dfs(1)
    return cnt


print(solution(5, [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 5], [3, 4], [4, 2], [4, 5]]))