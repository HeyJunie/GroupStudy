# 후위식 연산(postfix)
# https://reakwon.tistory.com/62

def solution(s):
    stack =[]
    for x in s:
        if x.isdecimal(): # isdecimal()은 숫자를 뽑아내는 함수
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
print(solution('532*+63/-'))