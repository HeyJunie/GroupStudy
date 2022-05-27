import collections
def solution(call):
    answer = ""
    tmp = call.lower()
    sH = collections.defaultdict(int)
    biggest = -1
    for x in tmp:
        sH[x] += 1
        if sH[x] > biggest:
            biggest = sH[x]
    for i, x in enumerate(tmp):
        if biggest > sH[x]:
            answer += call[i]
    return answer

s1 = "abcabcdefabc"
s2 = "abxdeydeabz"
s3 = "abcabca"
s4 = "ABCabcA"

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))