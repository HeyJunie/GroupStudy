# 번외 NHN 유치원

def solution(fight):
    graph = [[0] * 9 for _ in range(9)]
    for a,b in fight:
        graph[a][b] = 1
        graph[b][a] = 1
    ch = [0] * 9
    cnt = 0
    res = []
    def DFS(L):
        nonlocal cnt
        if L == 8:
            for k in range(7):
                if graph[res[k]][res[k+1]] == 1:
                    break
            else:
                cnt += 1
        else:
            for i in range(1, 9):
                if ch[i] == 0:
                    ch[i] = 1
                    res.append(i)
                    DFS(L+1)
                    ch[i] = 0
                    res.pop()
    DFS(0)
    return cnt

print(solution([[5, 3], [4, 3], [4, 7], [3, 6]]))