# 연속된 문자 지우기

def solution(s):
    answer = []
    stack = []

    for i in range(len(s)):
        stack.append(s[i])
        if s[i] == s[i+1]:
            stack.pop()
    print(stack)
    return answer

print(solution('acbbcaa'))
print(solution('bacccaba'))