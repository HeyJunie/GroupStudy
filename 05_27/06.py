def solution(words):
    answer = 0
    n = len(words)
    words.sort(key=lambda x : len(x))
    for i in range(n):
        for j in range(i+1, n):
            if isUnique(words[i], words[j]):
                tmp = len(words[i])*len(words[j])
                answer = max(answer, tmp)
    return answer

def isUnique(short, long):
    for x in short:
        if long.find(x) != -1:
            return False
    return True

s1 = ["skudy", "kstue", "time", "back", "good"]
s2 = ["kk", "k", "kkk", "kkkkk", "kkkk"]

print(solution(s1))
print(solution(s2))