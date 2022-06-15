# 프로그래머스 배달

import heapq


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])
    dist = [float('inf')] * (N + 1)
    dist[0] = 1
    tree = []
    heapq.heappush(tree, [0, 1])
    print(tree)
    while tree:
        nowtime, now = heapq.heappop(tree)
        for nv, time in graph[now]:
            if nowtime + time < dist[nv]:
                dist[nv] = nowtime + time
                heapq.heappush(tree, [dist[nv], nv])

    return
