# 최대 매출

def solution(nums, k):
    answer = 0
    sum = 0
    for i in range(k):
        sum += nums[i]
    answer = sum
    for i in range(k, len(nums)):
        sum += (nums[i] - nums[i-k])
        answer = max(answer, sum)
    return answer

print(solution([12, 15, 11, 20, 25, 10, 20, 19, 13, 15], 3))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([12, 34, 56, 72, 93, 121, 33, 11, 23, 52], 4))