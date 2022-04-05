# 스도쿠는 일본어로 "수독(數獨)"을 읽은 것이다.
# 이는 미국에서 유명한 일본의 한 퍼즐 이름이기도 하다.
# 스도쿠는 9x9 격자판에 다음 조건을 만족하여 수를 채워 넣는 게임이다.
#
# 각 정수 1-9는 각 행에 정확히 한 번씩 등장해야 한다.
# 각 정수 1-9는 각 열에 정확히 한 번씩 등장해야 한다.
# 각 정수 1-9는 각 작은 3x3 정사각형에 정확히 한 번씩 등장해야 한다.

# 남규는 스도쿠에 푹 빠져서 하루종일 스도쿠 문제를 풀던 와중,
# 스도쿠를 풀었지만 그것이 정답인지를 쉽게 확인할 수 없어 고민에 빠졌다.
# 불쌍한 남규를 위해 다 채워진 스도쿠 판이 올바른 답인지 판별하는 프로그램을 작성해 주자.
import sys

# def check_row():
#     while matrix[i] <= 9:
#
#
#     return
# def check_col():
#     return
# def check_sqr():
#     return
#
case = int(sys.stdin.readline())
matrix = []


for _ in range(case):
    for i in range(9):
        matrix.append(list(map(int, sys.stdin.readline().split())))


print(matrix)
