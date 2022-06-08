# 선긋기

def solution(nums):
    answer = 0
    nums.sort(key=lambda x: (x[0], x[1]))
    s = nums[0][0]
    e = nums[0][1]
    for i in range(1, len(nums)):
        if nums[i][0] <= e and nums[i][1] > e:
            e = nums[i][1]
        elif nums[i][0] > e:
            answer += e - s
            s = nums[i][0]
            e = nums[i][1]
    answer += e - s

    return answer


print(solution([[1, 3], [2, 5], [7, 10]]))
print(solution([[5, 6], [1, 3], [7, 8], [9, 10]]))