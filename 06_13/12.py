# 송아지 찾기

from collections import deque
from collections import defaultdict

def solution(s, e):
    deq = deque()
    deq.append(s)
    array = defaultdict(int)
    array[s] = 1
    L = 0
    while deq:
        length = len(deq)
        for _ in range(length):
            x = deq.popleft()
            for nx in [x - 1, x + 1, x + 5]:
                if array[nx] == 1:
                    continue
                if nx == e:
                    return L + 1
                array[nx] = 1
                deq.append(nx)
        L += 1

print(solution(5, 14))
print(solution(8, 3))