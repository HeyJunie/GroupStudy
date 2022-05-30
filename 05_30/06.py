# 바이토닉 수열

def solution(nums):
    answer = "YES"
    n = len(nums)
    i = 0
    while i + 1 < n and nums[i] < nums[i + 1]:
        i += 1
    if i == 0 or i == n - 1:
        return "NO"
    while i + 1 < n and nums[i] > nums[i + 1]:
        i += 1
    if i != n - 1:
        return "NO"

    return answer


nums1 = [1, 2, 3, 4, 5, 3, 1]
nums2 = [1, 3, 4, 5, 5, 6, 4, 3]
nums3 = [1, 2, 3, 4, 5]

print(solution(nums1))
print(solution(nums2))
print(solution(nums3))