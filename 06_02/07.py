# 연속된 자연수의 합

def solution(n):
    answer=0
    nums=range(1, n)
    s=0
    left=0
    for right in range(len(nums)):
        s+=nums[right]
        while s>n:
            s-=nums[left]
            left+=1
        if s==n:
            answer+=1

    return answer
print(solution(15))