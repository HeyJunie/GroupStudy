# 최대 길이 연속부분수열

def solution(nums, k):
    answer=0
    cnt=0
    left=0
    n=len(nums)
    for right in range(len(nums)):
        if nums[right]==0:
            cnt+=1
        while cnt>k:
            if nums[left]==0:
                cnt-=1
            left+=1
        answer=max(answer, right-left+1)

    return answer

print(solution([1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1], 2))