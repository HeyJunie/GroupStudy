# 최소 환승

from collections import deque
from collections import defaultdict


def solution(subway, s, e):
    graph = defaultdict(set)
    for i in range(len(subway)):
        for stop in subway[i]:
            graph[stop].add(i)
    ch = [0] * len(subway)
    deq = deque()
    deq.append(s)
    L = 0
    while deq:
        length = len(deq)
        # 레벨 탐색
        for i in range(length):
            curstop = deq.popleft()
            for line in graph[curstop]:
                if ch[line] == 1:
                    continue
                else:
                    ch[line] = 1
                    for stop in subway[line]:
                        if stop == e:
                            return L
                        deq.append(stop)
        L += 1
    return -1  # queue가 끝났을 때도 도착역에 도착할 수 없으면, -1 반환


print(solution([[1, 2, 3, 4, 5], [9, 7, 10], [7, 6, 3, 8]], 1, 10))
print(solution([[1, 2, 7], [3, 6, 7]], 1, 6))
print(solution([[7, 12], [5, 19], [7, 19], [9, 12, 13], [9, 5, 15]], 9, 19))