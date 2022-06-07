# 교육과정 설계

from collections import deque
def solution(need, plans):
    answer = []
    for plan in plans:
        deq = deque(need)
        for x in plan:
            if x in deq:
                if x != deq.popleft():
                    answer.append("NO")
                    break
        else:
            if len(deq) == 0:
                answer.append("YES")
            else:
                answer.append("NO")

    return answer

print(solution("CBA", ["CBDAGE", "FGCDAB", "CTSBDEA"])) # 출력 : ["YES", "NO", "YES"]
