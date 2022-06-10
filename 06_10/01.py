# 재귀함수를 이용한 이진수 출력

def solution(n):
    answer = []
    def dfs(k):
        if k == 0:
            return
        else:
            answer.append(n%2)
            dfs(n//2)
    dfs(n)
    return ''.join(map(str, answer))
print(solution(11))