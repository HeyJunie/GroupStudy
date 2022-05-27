def solution(s):
    answer = []
    for x in s:
        left = 0
        right = len(x)-1
        flag = 0
        while left < right:
            if x[left] != x[right]:
                flag = 1
                s1 = x[left:right]
                s2 = x[left+1:right+1]
                if s1 != s1[::-1] and s2 != s2[::-1]:
                    flag = 2
                break
            else:
                left += 1
                right -= 1
        answer.append(flag)
    return answer

# [0, 1, 1, 2, 2, 0, 1]
s = ["abba", "summuus", "xabba", "xabbay", "comcom", "comwwmoc", "comwwtmoc"]
print(solution(s))