# 공주 구하기

# 요세푸스 순열
# def solution(n, k):
#     nums = [i+1 for i in range(n)]
#     numIdx = 0
#     josephus = []
#
#     while len(nums):
#         #  0  1  2  3  4  5  6
#         # [1, 2, 3, 4, 5, 6, 7] -> 2 제거되는 값 numIdx = k-1 => numIdx = 3-1 = 2 % 7 = 2
#         # [1, 2, 4, 5, 6, 7] -> 4                             => numIdx = 2+3-1 = 4 % 6 = 4
#         # [1, 2, 4, 5, 7] -> 1                                => numIdx = 4+3-1 = 6 % 5 = 1
#         # [1, 4, 5, 7] -> 3                                   => numIdx = 1+3-1 = 3 % 4 = 3
#         # [1, 4, 5] -> 2                                      => numIdx = 3+3-1 = 5 % 3 = 2
#         # [1, 4] -> 0                                         => numIdx = 2+3-1 = 4 % 2 = 0
#         # [4] -> 0                                            => numIdx = 0+3-1 = 2 % 1 = 0
#         numIdx = (numIdx + k - 1) % len(nums)
#         removedNum = nums.pop(numIdx)
#         # 제거한 숫자를 받아와 요세푸스에 넣기
#         josephus.append(str(removedNum))
#
#     answer = josephus[-1]
#     return answer

from collections import deque
def solution(n, k):
    nums = range(1, n+1)
    deq = deque(nums)

    while deq:
        for _ in range(k-1):
            deq.append(deq.popleft())
        deq.popleft()
        if len(deq) == 1:
            return deq.popleft()

print(solution(8, 3))