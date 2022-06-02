# 수열의 경우수

def solution(nums):
    answer = 0
    peak = []
    low = []
    n = len(nums)
    for i in range(1, n-1):
        if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
            peak.append(i)

    for x in peak:
        left = x
        right = x
        lcnt = 0
        rcnt = 0
        while left >= 1 and nums[left+1] < nums[left]:
            lcnt += 1
            left -= 1
        while right < n-1 and nums[right] > nums[right+1]:
            rcnt += 1
            right += 1
        answer += (rcnt * lcnt)
    return answer

print(solution([1, 3, 2, 5, 7, 4, 2, 5, 1]))#6
print(solution([1, 2, 1, 2, 2, 7, 6, 5, 4, 5, 6, 7, 6, 3, 2, 1]))#16
print(solution([1, 2, 1, 2, 2, 5, 4, 3, 2, 3, 1]))#5