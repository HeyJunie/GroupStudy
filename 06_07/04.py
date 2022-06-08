# 연속된 문자 지우기

def solution(s):
    stack = []
    for x in s:
        if stack and stack[-1] == x: # stack이라고 적기만 해도 비어있지 않은 상태를 나타냄
            stack.pop()
        else:
            stack.append(x)

    return ''.join(stack)

print(solution('acbbcaa'))
print(solution('bacccaba'))