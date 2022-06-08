# 응급실

from collections import deque
def solution(risk, m):
    deq = deque(risk)
    standard = deq[m]
    count = 0
    n = len(risk)
    for i in range(n):
        if deq[0] < max(deq):
            deq.popleft()
            deq.append(deq[0])
        print(deq)

    return deq

print(solution([60, 50, 70, 80, 90], 2))