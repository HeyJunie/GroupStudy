# 키보드

# ASKII 코드 -> 대문자[65, 90], 소문자[97, 122], 숫자(0 - 9 문자형)[80, 89]
def solution(s, n):
    used = [0] * 27
    for ele in s:
        if ele.islower():
            used[ord(ele) - 97] = 1
        elif ele.isupper():
            used[26] = 1
            used[ord(ele) - 65] = 1

    cnt = 0
    for i in range(27):
        if used[i] == 1:
            cnt += 1

    if cnt <= n:
        return len(s)
    else:
        return -1

s1, n1 = "time to time", 5
s2, n2 = "time to study", 7
s3, n3 = "Big Life is Good", 10
s4, n4 = "Life is Good", 7

print(solution(s1, n1))
print(solution(s2, n2))
print(solution(s3, n3))
print(solution(s4, n4))