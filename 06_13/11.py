# 11. 이진트리 레벨 탐색(넓이 우선 탐색 : BFS)
# - 최단거리를 구해야 할 경우에 사용됨
# - 레벨별로 탐색을 한다.

from collections import deque

def solution(n):
    answer = ""
    deq = deque()
    deq.append(1)
    L = 0
    while deq:
        length = len(deq)
        for _ in range(length):
            v = deq.popleft()
            answer += str(v) + " "
            for nx in [v*2, v*2+1]:
                if nx > n:
                    continue
                deq.append(nx)
            L += 1
    return answer

print(solution(7))