# 영화 관람

# leetcode 739. Daily Temperatures 문제
# 주식 문제에서 사용 많이 됨
def solution(nums):
    n = len(nums)
    answer = [0] * n
    stack = []

    for i in range(n-1, -1, -1): # 뒤에서부터 비교할 예정
        while stack and nums[i] > nums[stack[-1]]:
            answer[stack[-1]] = i + 1
            stack.pop()
        stack.append(i)
    return answer

print(solution([50, 57, 52, 53, 51]))
print(solution([50, 46, 55, 76, 65, 50, 55, 53, 55, 50]))