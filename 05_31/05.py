# 임시반장 정하기

def solution(students):
    answer = 0
    n= len(students)
    cnt = 0
    maxN = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            for k in range(5):
                if students[i][k] == students[j][k]:
                    cnt += 1
                    break
        if cnt > maxN:
            maxN = cnt
            answer = i + 1

    return answer

print(solution([[2, 3, 1, 7, 3], [4, 1, 9, 6, 8], [5, 5, 2, 4, 4], [6, 5, 2, 6, 7], [8, 4, 2, 2, 2]]))