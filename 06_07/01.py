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

# def solution(s):
#     answer = "YES"
#     count = 0
#     for x in s:
#         if x == "(":
#             count += 1
#         else:
#             if count == 0:
#                 return "NO"
#             else:
#                 count -= 1
#     return "NO" if count == 0 else answer


print(solution('(()(()))(()'))
print(solution('(())()'))