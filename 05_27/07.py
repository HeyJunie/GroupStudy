import collections

# def solution(s):
#     answer = ""
#     sH = dict()
#     sH = collections.Counter(s) # Counter는 딕셔너리에 있는 모든 값을 세준다.
#     biggest = 0
#     for [key, val] in sH.items():
#         if val > biggest:
#             biggest = val
#             answer = key
#
#     return answer

def solution(s):
    answer = ""
    sH = collections.defaultdict(int) # 모든걸 0으로 초기화한다.
    for x in s:
        sH[x] += 1
    biggest = 0
    for key in sH:
        if sH[key] > biggest:
            biggest = sH[key]
            answer = key
    return answer


s1 = "BACBACCACCBDEDE"
s2 = "AAAAABBCCDDDD"

print(solution(s1))
print(solution(s2))