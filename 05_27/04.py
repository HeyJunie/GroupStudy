def solution(s):
    answer = "YES"
    # s = list(s)
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            s1 = s[left:right]
            s2 = s[left+1:right+1]

            if s1 != s1[::-1] and s2 != s2[::-1]:
                answer = 'NO'
            break
        else:
            left += 1
            right -= 1

    return answer

s1 = "abcbdcba"
s2 = "abcabbakcba"
s3 = "abcacbakcba"


print(solution(s1))
print(solution(s2))
print(solution(s3))