# 다익스트라 알고리즘

import heapq


def solution(n, edges, e):
    graph = [[] for _ in range(n + 1)]
    for a, b, c in edges:
        graph[a].append([b, c])  # a에서 b로 가는데 드는 비용이 c이다.
    tree = []
    heapq.heappush(tree, [0, 1])  # [0, 1] 출발 정점에서 1번 노드까지 가는 비용이 0
    dist = [1000] * (n + 1)
    dist[1] = 0
    while tree:
        nowcost, now = heapq.heappop(tree)  # now라는 정점까지 가는데 드는 비용 nowcost
        if nowcost > dist[now]:
            continue
        for nv, cost in graph[now]:
            # now에서 nv로 가는 비용
            if nowcost + cost < dist[nv]:
                dist[nv] = nowcost + cost
                heapq.heappush(tree, [dist[nv], nv])
    print(dist)
    return -1 if dist[e] == 1000 else dist[e]


print(solution(6, [[1, 2, 12], [1, 3, 4], [2, 1, 2], [2, 3, 5], [2, 5, 5], [3, 4, 5], [4, 2, 2], [4, 5, 5],
                   [6, 4, 5]], 5))