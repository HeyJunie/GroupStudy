# 타일 점프

from collections import deque
def solution(nums):
    n = len(nums)
    answer = -1
    deq = deque()
    deq.append(0)
    ch = [0] * n
    ch[0] = 1
    L = 0
    while deq:
        length = len(deq)
        for _ in range(length):
            x = deq.popleft()
            jump = nums[x]
            for i in range(1, jump + 1):
                nx = x + i
                if nx == n-1:
                    return L+1
                if nx < n and ch[nx] == 0:
                    ch[nx] = 1
                    deq.append(nx)
        L += 1
    return answer

print(solution([2, 2, 0, 2, 1, 1]))
print(solution([1, 0, 1, 1, 3, 1, 2, 1]))