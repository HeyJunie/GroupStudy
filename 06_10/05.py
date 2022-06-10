# 바둑이 승차

def solution(nums, w):
    answer = 0

    def dfs(L, s):
        nonlocal answer
        if w < s:
            return
        if L == len(nums):
            answer = max(answer, s)
        else:
            dfs(L + 1, s + nums[L])
            dfs(L + 1, s)

    dfs(0, 0)
    return answer


print(solution([81, 58, 42, 33, 61], 259))
print(solution([34, 56, 55, 67, 33, 76, 63, 43], 379))