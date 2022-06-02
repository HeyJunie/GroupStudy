def solution(money, nums):
    answer = 0
    partial_sum = 0
    left = 0
    for right in range(len(nums)):
        partial_sum += nums[right]

        while partial_sum > money:
            partial_sum -= nums[left]
            left += 1
        answer = max(answer, (right - left + 1))

    return answer

print(solution(420, [0, 900, 0, 200, 150, 0, 30, 50])) #5
print(solution(100, [245, 317, 151, 192])) #0