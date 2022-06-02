# 최대길이 바이토닉

def solution(nums):
    answer = 0
    peak = []
    n = len(nums)
    for i in range(1, n-1):
        if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
            peak.append(i)
            print(peak)
    for x in peak:
        left = x
        right = x
        cnt = 1
        while left >= 1 and nums[left-1] < nums[left]:
            cnt += 1
            left -= 1
        while right < n-1 and nums[right + 1] < nums[right]:
            cnt += 1
            right += 1
        answer = max(answer, cnt)
    return answer

nums = [1, 3, 2, 5, 7, 4, 2, 5, 1]

print(solution(nums))