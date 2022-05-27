import collections
def solution(s):
    sH = collections.Counter(s) # Counter는 딕셔너리에 있는 모든 값을 세준다.

    for key, val in enumerate(s):
        if sH[val] == 1:
            return  key+1
    return -1


s1 = "statitsics"
s2 = "aabb"
s3 = "stringshowtime"

print(solution(s1))
print(solution(s2))
print(solution(s3))