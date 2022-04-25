# 문제
# 진구는 친구들과 제로섬 게임을 하려고 한다.
#
# 제로섬 게임은 N개의 서로 다른 정수로 이루어진 리스트가 주어졌을 때,
# 더 적은 개수의 수를 더해서 0으로 만들면 이기는 게임이다.
#
# 진구는 친구들이 찾은 답이 최적의 답인지 검증하기 위해, 몇 개의 정수를 더해야 하는지 구하는 프로그램을 만들고자 한다.
#
# 입력 설명
# 길이가 1000 이하인 정수로 이루어진 리스트
#
# 출력 설명
# 총 합을 0으로 만드는 최소의 정수 개수
#
# 단, 답이 5보다 크거나 없는 경우 -1
#
# 입력 예시
# [-5, -2, 4, 5, 7]
#
# 출력 예시
# 2

# def solution(nums):
#     n = len(nums)
#     sum_num = []
#     len_list = []
#     list_set = [[nums[k] for k in range(n) if i&1<<k] for i in range(2**n)]
#     for i in range(len(list_set)):
#         sum_num.append(sum(list_set[i]))
#
#         if sum_num[i] == 0 and len(list_set[i]) > 0:
#             len_list.append(list_set[i])
#             answer = len(len_list[0])
#         elif sum_num[i] != 0 and len(list_set[i]) > 5:
#             answer = -1
#     return answer


from itertools import combinations

def solution(nums):
    n = len(nums)
    for i in range(1, 5):
        for indices in combinations(range(n), i):
            summation = 0
            for index in indices:
                summation += nums[index]
                if summation == 0:
                    return i
    return -1

nums = [-5, -2, 4, 3, 8]
print(solution(nums))

