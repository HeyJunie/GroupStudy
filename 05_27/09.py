import collections
def solution(s):
    answer = []
    sH = collections.Counter(s)
    biggest = float("-inf") # float("inf) => 양의 무한대, float("-inf") => 음의 무한대
    for x in "abc":
        if sH[x] > biggest:
            biggest = sH[x]
    for x in "abc":
        answer.append(biggest-sH[x])

    return answer


s1 = "aaabc"
s2 = "aabb"
s3 = "abc"

print(solution(s1))
print(solution(s2))
print(solution(s3))