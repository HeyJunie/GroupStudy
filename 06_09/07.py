# 팀 구성

def solution(abilities, k):
    answer = 0
    n = len(abilities)
    diff = []
    abilities.sort(reverse=True)
    if n % 2 != 0:
        abilities.append(0)
        n = len(abilities)
    for i in range(n // 2):
        diff.append(abilities[i * 2] - abilities[i * 2 + 1])
    diff.sort(reverse=True)

    for i in range(n // 2):
        answer += abilities[i * 2 + 1]

    for i in range(k):
        answer += diff[i]

    return answer


print(solution([2, 8, 3, 6, 1, 9, 1, 9], 2))
print(solution([7, 6, 8, 9, 10], 1))