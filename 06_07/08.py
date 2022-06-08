# 좋은 단어

from collections import deque
# def solution(s, m):
#     s = deque(s)
#     cnt = 0
#     for i in range(len(s)):
#         a = s.popleft()
#         if len(s) > m:
#             for j in range(m):
#                 if len(s[j]) == len(a):
#                     cnt += 1
#         else:
#             for j in range(len(s)):
#                 if len(s[j]) == len(a):
#                     cnt += 1
#     return cnt

def solution(s, m):
    answer = 0
    Nlist = [deque() for _ in range(21)] # 각 단어의 길이가 20을 넘지 않는다.

    for i, name, in enumerate(s):
        # print(Nlist)
        L = len(name)
        while Nlist[L] and i-Nlist[L][0] > m:
            Nlist[L].popleft()
        answer += len(Nlist[L])
        Nlist[L].append(i)
        # print(Nlist)

    return answer

print(solution(["back", "seen", "big", "good", "size"], 2))
print(solution(["back", "seen", "good", "size"], 2))