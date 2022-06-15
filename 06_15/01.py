# 다익스트라 알고리즘

def solution(n, edges, e):
    graph = [[] for _ in range(n+1)]
    ch = [0] * (n+1)
    for a, b, c in edges:
        graph[a].append([b, c]) # a에서 b로 가는데 드는 비용이 c이다.
    dist = [1000] * (n+1)
    dist[1] = 0
    for i in range(n):
        minP = 0
        for j in range(1, n+1):
            if ch[j] == 0 and dist[j] < dist[minP]:
                minP = j
        ch[minP] = 1
        for nv, cost in graph[minP]:
            if dist[minP] + cost < dist[nv]: # 출발 정점에서 이전 정점값보다 작으면 바꿔준다.
                dist[nv] = dist[minP] + cost
    print(dist)
    return dist[e]

print(solution(6, [[1, 2, 12], [1, 3, 4], [2, 1, 2], [2, 3, 5], [2, 5, 5], [3, 4, 5], [4, 2, 2], [4, 5, 5],
[6, 4, 5]], 5))