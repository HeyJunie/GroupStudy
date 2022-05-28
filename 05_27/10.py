import collections
def solution(s):
    answer = []
    sH = collections.Counter(s)
    count = 0
    for x in sH:
        if sH[x] % 2 == 1:
            count += 1

    return len(s) - count + 1 if count > 0 else len(s)


s1 = "abcbbbccaa"
s2 = "abcde"
s3 = "ccc"

print(solution(s1))
print(solution(s2))
print(solution(s3))