# 마지막 남은 수

import heapq
def solution(nums):
    answer = 0
    maxH = []
    for x in nums:
        heapq.heappush(maxH, -x)
    while len(maxH) > 1:
        a = - heapq.heappop(maxH)
        b = - heapq.heappop(maxH)
        if a != b :
            heapq.heappush(maxH, -(a-b))
    if len(maxH) > 0:
        answer = -heapq.heappop(maxH)
    return answer

print(solution([5, 2, 4, 3, 1]))
print(solution([7, 6, 3, 2, 4, 5, 1]))