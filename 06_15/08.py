# 바둑 대회

def solution(nums):
    answer = float('inf')
    n = len(nums)
    ch = [0] * n
    combi = []
    def dfs(L, s):
        nonlocal n, answer
        if L == n//2:
            a = []
            b = []
            for i in range(n):
                if ch[i] == 1:
                    a.append(i)
                else:
                    b.append(i)
            aSum = 0
            bSum = 0
            for j in range(n//2):
                aSum += nums[a[j]][0]
                bSum += nums[b[j]][1]
            answer = min(answer, abs(aSum - bSum))
        else:
            for i in range(s, n):
                ch[i] = 1
                dfs(L+1, i+1)
                ch[i] = 0
    dfs(0, 0)
    return answer

print(solution([[87, 84], [66, 78], [94, 94], [93, 87], [72, 92], [78, 63]]))