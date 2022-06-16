# 친구인가? (Disjoint-Set : Union&Find)

def solution(n, nums, s1, s2):
    answer = "YES"
    unf = [i for i in range(0, n + 1)]

    def find(v):
        if v == unf[v]:
            return v
        else:
            unf[v] = find(unf[v])
            return unf[v]

    def Union(a, b):
        fa = find(a)
        fb = find(b)
        if fa != fb:
            unf[fa] = fb

    for a, b in nums:
        Union(a, b)
    if find(s1) != find(s2):
        return "NO"
    return answer


print(solution(9, [[1, 2], [2, 3], [3, 4], [1, 5], [6, 7], [7, 8], [8, 9]], 3, 8))