# 쇠막대기

def solution(s):
    stack = []
    bars = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
#             print(stack)
        else:
            stack.pop()
#             print(stack)
            if s[i-1] == '(':
                bars += len(stack)
            else:
                bars += 1
#         print(stack, bars)
    return bars

print(solution('()(((()())(())()))(())'))
print(solution('(((()(()()))(())()))(()())'))