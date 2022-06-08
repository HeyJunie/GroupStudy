# 침몰하는 타이타닉

def solution(nums, m):
    answer = 0
    n = len(nums)
    lt = 0
    rt = n - 1
    nums.sort()
    while lt <= rt:
        if nums[lt] + nums[rt] <= m:
            answer += 1
            lt += 1
            rt -= 1
        else:
            answer += 1
            rt -= 1
    return answer


print(solution([90, 50, 70, 100, 60], 140))

