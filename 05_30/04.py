# 가장 높은 증가수열

def solution(nums):
    answer=0
    height=0
    n=len(nums)
    for i in range(1, n):
        if nums[i-1]<nums[i]:
            height+=(nums[i]-nums[i-1])
        else:
            answer=max(answer, height)
            height=0
    answer=max(answer, height)
    return answer

nums1 = [5, 2, 4, 7, 7, 3, 9, 10, 11]
nums2 = [8, 12, 2, 3, 7, 6, 20, 3]

print(solution(nums1))
print(solution(nums2))