import collections
# def solution(words):
#     answer = list(words[0])
#     for i in range(1, len(words)):
#         comparison = words[i]
#         common_chars = []
#         for char in comparison:
#             if char in answer:
#                 common_chars.append(char)
#                 answer.remove(char)
#         answer = common_chars
#
#     return answer

def solution(words):
    sH = collections.Counter(words[0])
    for word in words:
        sH &= collections.Counter(word)
        # 비트 연산자 개념 : 1&1 = 1, 1&0 = 0, 0&1= 0, 0&0 = 0

    answer = []
    for key, val in sH.items():
        answer += key * val

    return answer


# counts Counter({'s': 2, 'e': 2, 't': 1, 'a': 1, 'u': 1})
# counts Counter({'s': 2, 'e': 1, 'a': 1, 'u': 1})
# counts Counter({'s': 2, 'e': 1, 'a': 1})


s1 = ["steasue", "sasseysu", "kseseas"]
s2 = ["ackky", "kabck", "yokkcs"]
s3 = ["longlong", "longtong", "longbig"]

print(solution(s1))
print(solution(s2))
print(solution(s3))