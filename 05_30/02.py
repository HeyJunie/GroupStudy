# 제곱수 정렬
# def solution(nums):
#     answer = []
#     sort = []
#     for i in range(len(nums)):
#         x = nums[i]**2
#         sort.append(x)
#         k = len(nums) - i
#         for j in range(1, k):
#             if nums[j - 1] >= nums[j]:
#                 temp = nums[j - 1]
#                 nums[j - 1] = nums[j]
#                 nums[j] = temp
#                 answer.append(nums[j])
#     return answer

def solution(nums):
    n = len(nums)
    answer = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            tmp = nums[right]
            right -= 1
        else:
            tmp = nums[left]
            left += 1
        answer[i] = tmp * tmp

    return answer

nums1 = [-4, -1, 0, 3, 10]
nums2 = [-7, -3, 2, 3, 11]

print(solution(nums1))
print(solution(nums2))