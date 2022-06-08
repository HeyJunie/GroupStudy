# 회의실 배정

def solution(times):
    answer = 0
    times.sort(key=lambda x : (x[1], x[0])) # 시작 시간과 끝나는 시간이 같은 경우가 있으므로
    et = 0
    for s, e in times:
        if s >= et:
            et = e
            answer += 1
    return answer

print(solution([[1, 4], [2, 3], [3, 5], [4, 6], [5, 7]]))