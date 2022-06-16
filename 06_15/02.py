# Floyd warshall

def solution(n, edges):
    answer = 0
    dist = [[100000] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for a, b, c in edges:
        dist[a][b] = c
        # i -> K -> j : i에서 j까지 가는데 K라는 정점을 통해서 가는게 더 좋은지 확인
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    print(dist)

    return answer


print(solution(5, [[1, 2, 6], [1, 3, 3], [3, 2, 2], [2, 4, 1], [2, 5, 13], [3, 4, 5], [4, 2, 3], [4, 5,
                                                                                                  7]]))