# 이진트리 순회(깊이 우선 탐색 : DFS)

# 전위 순회
def solution(n):
    def dfs(v):
        if v > 7:
            return
        else:
            print(v, end=' ')
            dfs(v * 2)
            dfs(v * 2 + 1)

    dfs(n)

print(solution(1))