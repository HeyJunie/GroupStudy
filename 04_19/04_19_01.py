# 문제
# N×N의 표에 수 N2개 채워져 있다. 채워진 수에는 한 가지 특징이 있는데,
# 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다. N=5일 때의 예를 보자.
#
# 12	7	9	15	5
# 13	8	11	19	6
# 21	10	26	31	16
# 48	14	28	35	25
# 52	20	32	41	49
#
# 이러한 표가 주어졌을 때, N번째 큰 수를 찾는 프로그램을 작성하시오. 표에 채워진 수는 모두 다르다.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,500)이 주어진다. 다음 N개의 줄에는 각 줄마다 N개의 수가 주어진다.
# 표에 적힌 수는 -10억보다 크거나 같고, 10억보다 작거나 같은 정수이다.
#
# 출력
# 첫째 줄에 N번째 큰 수를 출력한다.

# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
# nums = deque()
#
# for _ in range(n):
#     nums.append(deque(map(int, sys.stdin.readline().rstrip().split())))
#
# list = []
# for i in range(n):
#     for j in range(n):
#         list.append(nums[i][j])
# list.sort(reverse=True)
#
# print(list[n-1])
import sys
import heapq

# nxn 보드 입력
n = int(sys.stdin.readline())
# 힙 숫자들의 리스트
num_list = []
for _ in range(n):
    # n번 숫자들을 입력 받음
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))

    # 저장할 리스트에 값이 없으면
    if not num_list:
        # 입력 받은 숫자들을 하나씩
        for num in numbers:
            # num_list에 숫자(num)를 넣는다.
            # heappush를 이용해서 리스트에 최솟값부터 담긴다.
            heapq.heappush(num_list, num)
            # print(num_list)

    else:
        for num in numbers:
            # 만약 리스트 내에서 최솟값이 입력 받은 수보다 작으면
            if num_list[0] < num:
                # 입력 받은 수를 num_list에 넣어준다.
                heapq.heappush(num_list, num)
                # print(num_list)
                # 그리고 최솟값(num_list[0])을 하나씩 제거
                heapq.heappop(num_list)
                # print(num_list)
# print(num_list) -> 최솟값들을 하나씩 제거하고나면, num_list에는 가장 큰 수 n개가 순서대로 남아 있다.
print(num_list[0])


# def heapsort(iterable):
#     h = []
#     result = []
#
#     for value in iterable:
#         heapq.heappush(h, value)
#
#     for _ in range(len(h)):
#         result.append(heapq.heappop(h))
#
#     return result
