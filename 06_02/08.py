# 사과

def solution(apples, power, m):
    answer=0
    s=0
    for i in range(len(power)):
        if power[i]==1:
            s+=apples[i]
    for i in range(m-1):
        if power[i]==0:
            s+=apples[i]

    left = 0
    for right in range(m-1, len(power)):
        if power[right]==0:
            s+=apples[right]
        answer=max(answer, s)
        if power[left]==0:
            s-=apples[left]
        left+=1

    return answer

print(solution([3, 2, 1, 2, 1, 3], [1, 0, 0, 1, 0, 0], 3))