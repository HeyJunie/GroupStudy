# from collections imporight deque
# def solution(s):
#     answer = ""
#     s = s.lower()
#     deq = deque()
#     deq.append(s)
#
#     for i in range(len(s)):
#         if s[i] == s[-1]:
#             if len(deq) != 0:
#                 deq.pop()
#             else:
#                 answer = "YES"
#         else:
#             answer = "NO"
#
#     return answer
#
# s1 = "gooG"
# s2 = "Moon"
#
# print(solution(s1))
# print(solution(s2))


def solution(s):
    answer = "YES"
    s = s.lower()
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return "NO"
        else:
            left += 1
            right -= 1

    return answer

s1 = "gooG"
s2 = "Moon"

print(solution(s1))
print(solution(s2))