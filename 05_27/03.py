def solution(s):
    answer = list(s)
    left = 0
    right = len(s)-1

    while left < right:
        if answer[left] != s.isalpha():
            left += 1
        elif answer[right] != s.isalpha():
            right -= 1
        else:
            tmp = answer[left]
            answer[left] = answer[right]
            answer[right] = tmp
            left += 1
            right -= 1

    return "".join(answer)

s1 = "a#b!GE*T@S"
s2 = "###ab*@@Sty"

print(solution(s1))
print(solution(s2))