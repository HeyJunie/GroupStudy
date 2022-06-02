# 연속 부분수열 2

def solution(nums, m):
    answer = 0
    partial_sum = 0
    left = 0
    for right in range(len(nums)):
        partial_sum += nums[right]
        while partial_sum > m:
            partial_sum -= nums[left]
            left += 1
        answer += (right-left+1) # left부터 right까지 갯수를 셀 때도 사용될 수 있음

    return answer

print(solution([1, 3, 1, 2, 3], 5))
print(solution([1, 1, 1, 1, 1, 1], 3))
print(solution([1, 1, 2, 2, 1, 2, 1, 3, 2], 5))