# 순열 구하기

def solution(nums, m):
    answer = []
    n = len(nums)
    tmp = []
    ch = [0] * n
    def dfs(L):
        if L == m:
            answer.append(tmp.copy())
        else:
            for i in range(n):
                if ch[i] == 0:
                    ch[i] = 1
                    tmp.append(nums[i])
                    dfs(L+1)
                    ch[i] = 0
                    tmp.pop()

    dfs(0)
    return answer
print(solution([3, 6, 9], 2))