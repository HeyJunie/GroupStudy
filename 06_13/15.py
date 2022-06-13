# 가장 가까운 큰 수

def solution(n):
    answer = 0
    nums = []
    tmp = n
    while tmp > 0:
        t = tmp % 10
        nums.append(t)
        tmp = tmp // 10
    nums.sort()

    length = len(nums)
    ch = [0] * length
    p = []
    flag = 0
    def dfs(L):
        nonlocal answer, flag
        if flag == 1:
            return

        if L == length:
            answer = 0
            for i in range(L):
                answer = answer * 10 + p[i]
            if answer > n:
                flag = 1
        else:
            for i in range(length):
                if ch[i] == 0:
                    ch[i] = 1
                    p.append(nums[i])
                    dfs(L+1)
                    ch[i] = 0
                    p.pop()
    dfs(0)
    if flag == 0:
        return -1
    return answer

print(solution(123))
print(solution(321))
print(solution(20573))