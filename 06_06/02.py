# 괄호문자제거

# import re
# def solution(s):
#     pattern = '\([^)]*\)'
#     text = re.sub(pattern=pattern, repl='', string=s)
#     answer = ''.join(text)
#     return answer

def solution(s):
    answer = []
    stack = []
    for x in s:
        if x == "(":
            stack.append(x)
        elif x == ")":
            stack.pop()

        if x != "(" and x != ")" and len(stack) == 0:
            # if len(stack) == 0:
            answer.append(x)

    return ''.join(answer)

print(solution("(A(BC)D)EF(G(H)(IJ)K)LM(N)"))