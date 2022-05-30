# 가장 긴 수열
#
# def solution(nums):
#     answer = 0
#     standard = nums[0]
#     part = []
#     for i in range(1, len(nums)-1):
#         if nums[i] < nums[0] or nums[i] > nums[0]:
#             part.append(nums[0])
#     return  answer

def solution(nums):
    answer=0
    up=1
    down=1
    maxup=0
    maxdown=0
    for i in range(1, len(nums)):
        if nums[i-1]<nums[i]:
            up+=1
        else:
            maxup=max(maxup, up)
            up=1
        if nums[i-1]>nums[i]:
            down+=1
        else:
            maxdown=max(maxdown, down)
            down=1

    maxup=max(maxup, up)
    maxdown=max(maxdown, down)
    answer=max(maxup, maxdown)
    return answer

nums1 = [5, 3, 6, 7, 9, 8, 5, 3, 1, 2, 3, 4, 5, 6, 7]
nums2 = [1, 2, 3, 3, 4, 5, 6, 7, 7]

print(solution(nums1))
print(solution(nums2))