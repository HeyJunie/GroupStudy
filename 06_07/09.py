# 가장 큰 수

def solution(nums, m):
    stack = []
    nums = str(nums)  # 숫자를 하나하나 비교할 수 있도록 바꿔야 한다.
    for x in nums:
        while stack and m > 0 and stack[-1] < x:
            # stack에 숫자를 전체 숫자에서 m개 제거한 만큼까지만 제거한 자릿수를 만든다.
            stack.pop()
            m -= 1
        stack.append(x)

    if m != 0:
        stack = stack[0:-m]

    return ''.join(stack)

print(solution(5276823, 3))
print(solution(9977252641, 5))