# 결혼식

def solution(times):
    answer = 0
    cnt = 0
    rec = []
    for i, o in times:
        rec.append((i, 2))
        rec.append((o, 1))
    rec.sort(key=lambda x: (x[0], x[1]))

    for x in rec:
        if x[1] == 1:
            cnt -= 1
        else:
            cnt += 1
            answer = max(answer, cnt)
    return answer


print(solution([[14, 18], [12, 15], [15, 20], [20, 30], [5, 14]]))