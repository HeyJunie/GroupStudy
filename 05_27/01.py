def solution(s):
    answer = ""
    s = s + ' '
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            answer += s[i]
            if count > 1:
                answer += str(count)
            count = 1

    return answer

s1 = "KKHSSSSSSSE"
s2 = "AAABCCCDD"

print(solution(s1))
print(solution(s2))
