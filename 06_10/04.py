# 합이 같은 부분집합

def solution(nums):
    answer = "NO"
    n = len(nums)
    total = sum(nums)
    flag = 0

    def dfs(L, s):
        nonlocal answer, flag
        if flag == 1:
            return
        if L == n:  # 어떤 부분집합의 합을 완성시킴
            if (total - s) == s:
                answer = "YES"
                flag = 1
        else:
            dfs(L + 1, s + nums[L])
            dfs(L + 1, s)

    dfs(0, 0)
    return answer


print(solution([1, 3, 5, 6, 7, 10]))
print(solution([5, 2, 6, 9, 10, 12]))
print(solution([3, 9, 11, 13]))