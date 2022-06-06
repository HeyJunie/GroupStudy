# 올바른 괄호

def solution(s):
    answer = "YES"
    stack = []
    for x in s:
        if x == "(":
            stack.append(x)
        else:
            if len(stack) == 0:
                return "NO"
            else:
                stack.pop()

    return "NO" if len(stack) else answer

print(solution('(()(()))(()'))
print(solution('(())()'))