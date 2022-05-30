# 수열 축소
# def repeat(nums):
#     answer = []
#     for i in range(len(nums) - 1):
#         answer.append(nums[i + 1] - nums[i])
#     return answer
#
# def solution(nums, m):
#     answer = []
#     for i in range(m):
#         x = repeat(nums)
#         answer.append(x)
#     return answer

def solution(nums, m):
    answer = []
    n = len(nums)
    for i in range(m):
        for j in range(n - i - 1):
            nums[j] = nums[j + 1] - nums[j]
    answer = nums[:n - m]

    return answer

nums = [5, 3, 7, 9, -2]
m = 2

print(solution(nums, m))