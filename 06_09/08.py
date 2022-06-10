# 최소힙

import heapq
def solution(nums):
    answer = []
    minH = []
    for x in nums:
        if x == 0:
            if len(minH) == 0:
                answer.append(-1)
            else:
                answer.append(heapq.heappop(minH))
        else:
            heapq.heappush(minH, x)
    return answer

print(solution([5, 3, 6, 0, 5, 0, 2, 4, 0, -1]))