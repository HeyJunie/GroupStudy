# 원더 랜드(최소 스패닝 트리 : 크루스칼, Union&Find)

def solution(n, edges):
    answer = 0
    unf = [i for i in range(0, n + 1)]
    edges.sort(key=lambda x: x[2])  # 간선값으로 정렬

    def find(v):
        if unf[v] == v:
            return v
        else:
            unf[v] = find(unf[v])
            return unf[v]

    def union(a, b):
        fa = find(a)
        fb = find(b)
        if fa != fb:
            unf[fa] = fb

    cnt = 0
    for a, b, c in edges:
        fa = find(a)
        fb = find(b)
        if fa != fb:
            answer += c
            unf[fa] = fb
            cnt += 1
            if cnt == n - 1:
                break
    return answer


print(solution(9, [[1, 2, 12], [1, 9, 25], [2, 3, 10], [2, 8, 17], [2, 9, 8], [3, 4, 18], [3, 7, 55], [4,
                                                                                                       5, 44],
                   [5, 6, 60], [5, 7, 38], [7, 8, 35], [8, 9, 15]]))