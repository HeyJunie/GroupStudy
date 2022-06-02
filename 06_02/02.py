# 매출액의 종류
import collections
def solution(nums, k):
    answer = []
    nH = collections.defaultdict(int)
    n = len(nums)
    for i in range(k-1):
        nH[nums[i]] += 1
    left = 0
    # 윈도우 크기 정의
    for right in range(k-1, n):
        nH[nums[right]] += 1
        answer.append(len(nH))
        nH[nums[left]] -= 1
        if nH[nums[left]] == 0:
            del nH[nums[left]]
        left += 1

    return answer

print(solution([20, 12, 20, 10, 23, 17, 10], 4))
print(solution([1, 2, 3, 2, 2, 3, 3, 3, 3, 2], 3))
