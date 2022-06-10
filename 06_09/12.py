# 작업 스케줄

import heapq
def solution(tasks):
    answer = 0
    tasks.sort(key=lambda x : x[1])
    time = 0
    maxH = []
    for x in tasks:
        if time + x[0] <= x[1]:
            heapq.heappush(maxH, -x[0])
            time += x[0]
        elif len(maxH) > 0 and -maxH[0] > x[0]:
            time += (x[0] - (-heapq.heappop(maxH)))
            heapq.heappush(maxH, -x[0])
    print(tasks)
    answer = len(maxH)
    return answer
print(solution([[3, 11], [5, 10], [3, 10], [2, 10], [4, 12]]))