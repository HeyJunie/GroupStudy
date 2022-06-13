# 씨름선수(그리디)

def solution(players):
    answer = 0
    maxW = 0
    players.sort(reverse = True)
    for x, y in players:
        if y > maxW:
            answer += 1
            maxW = y
    return answer

print(solution([[172, 67], [183, 65], [180, 70], [170, 72], [180, 60]]))