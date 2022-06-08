# 동전교환

# 동전들이 전부 배수 관계에 있을 때는 그리디, 그렇지 않은 경우에는 다이나믹을 이용한다.
def solution(nums, m):
    n = len(nums)
    count = 0
    for i in range(n):
        while m % nums[-1] != 0:
            count += 1


print(solution([1, 5, 10], 15))