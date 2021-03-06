# 문제
# 4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.
#
# 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
# 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
# X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
# 예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다.
# 우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다.
#
# ‘()’ 인 괄호열의 값은 2이다.
# ‘[]’ 인 괄호열의 값은 3이다.
# ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
# 예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자.
# ‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로 ‘(()[[]])’의 괄호값은 2×11=22 이다.
#     그리고 ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.
#
# 여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다.
#
# 입력
# 첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.
#
# 출력
# 첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다.

import sys
from collections import deque

# 괄호 입력
# 앞에서부터 빼주며 비교하기 위해
bracket = deque(sys.stdin.readline().strip())
# print(bracket)

# 괄호 안의 요소들을 하나씩 비교
def cal(start):
    # 값을 더해줄 변수 설정
    br_result = 0
    while bracket:
        # 괄호들에서 왼쪽부터 하나씩 빼서 반환할 변수
        # 하나씩 빼서 나열한 값들이 존재한다.
        after_pop = bracket.popleft()

        # 시작하는 괄호과 뺀 괄호가 각각 모두 존재한다면,
        if start == '(' and after_pop == ')':
            # 만약 둘 다 존재한다면, 1보다 큰 수일 것이고, 그 큰 수에 2를 곱한 값을 반환
            # 아니면 1 값을 최대값으로 반환하여 더하는 값을 2로 반환한다.
            br_result = 2 * max(1, br_result)
            return br_result
        elif start == '[' and after_pop == ']':
            br_result = 3 * max(1, br_result)
            return br_result
        # 만약 여는 괄호가 ( 거나 [ 둘 중에 하나면, 재귀함수를 통해 다시 함수를 돌린다.
        elif after_pop == '(' or after_pop == '[':
            br_result += cal(after_pop)
    # 잘못된 괄호일 경우에 0을 내보낸다.
    print(0)
    # 파이썬의 코드를 끝나는 즉시 중단
    sys.exit()

# 최종값을 더해줄 변수
result = 0
# for _ in range(len(bracket)):
#     result += cal(bracket.popleft())
while bracket:
    result += cal(bracket.popleft())

print(result)