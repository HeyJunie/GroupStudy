# 거리 두기

# def solution(nums):
#     answer = 0
#     count = 0
#     for i in nums:
#         if i == 0:
#             count+= 1
#         elif i == 1:
#             count = 0
#
#
#     return  answer

def solution(nums):
    answer=0
    n=len(nums)
    dist=[0]*n
    d=1000
    for i in range(n):
        if nums[i]==1:
            d=0
            dist[i]=d
        else:
            d+=1
            dist[i]=d
    d=1000
    for i in range(n-1, -1, -1):
        if nums[i]==1:
            d=0
        else:
            d+=1
            dist[i]=min(dist[i], d)
    answer=max(dist)
    return answer

nums = [1, 0, 0, 0, 1, 0, 0, 1, 0, 1]

print(solution(nums))