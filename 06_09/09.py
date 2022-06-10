# 최대힙

import heapq
def solution(nums):
    answer = []
    maxH = []
    for x in nums:
        if x == 0:
            if len(maxH) == 0:
                answer.append(-1)
            else:
                answer.append(-heapq.heappop(maxH))
        else:
            heapq.heappush(maxH, -x)
    return answer

print(solution([5, 3, 6, 0, 5, 0, 2, 4, 0, -1]))