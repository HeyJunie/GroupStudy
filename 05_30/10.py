# 수열의 경우수

def solution(nums):
    answer=0
    peaks=[]
    n=len(nums)
    for i in range(1, n-1):
        if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
            peaks.append(i)
    for pos in peaks:
        lt=pos
        rt=pos
        lcnt=0
        rcnt=0
        while lt>=1 and nums[lt-1]<nums[lt]:
            lcnt+=1
            lt-=1
        while rt<n-1 and nums[rt]>nums[rt+1]:
            rcnt+=1
            rt+=1
        answer+=(lcnt*rcnt)
    return answer

print(solution([1, 3, 2, 5, 7, 4, 2, 5, 1]))#6
print(solution([1, 2, 1, 2, 2, 7, 6, 5, 4, 5, 6, 7, 6, 3, 2, 1]))#16
print(solution([1, 2, 1, 2, 2, 5, 4, 3, 2, 3, 1]))#5