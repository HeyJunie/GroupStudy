# 후위식 연산(postfix)
# https://reakwon.tistory.com/62

import re
def solution(s):
    stack =[]
    for x in s:
        if x in re.sub(r'[^0-9]', '', s):
            stack.append(int(x))

        if x == '+':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 + num1)
        elif x == '-':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 - num1)
        elif x == '*':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 * num1)
        elif x == '/':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 / num1)

    return stack[0]

print(solution('352+*9-'))