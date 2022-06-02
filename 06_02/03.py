# 연속 부분수열 1

def solution(nums, m):
    answer = 0
    partial_sum = 0
    left = 0
    for right in range(len(nums)):
        partial_sum += nums[right]
        while partial_sum > m:
            partial_sum -= nums[left]
            left += 1
        if partial_sum == m:
            answer += 1

    return answer

print(solution([1, 2, 1, 3, 1, 1, 1, 2], 6))
print(solution([1, 1, 1, 1, 1, 1], 3))