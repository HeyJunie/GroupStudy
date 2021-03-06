# 문제
# 차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다.
# 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에,
# 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다.
# 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
# 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어,
# 그 배추들 역시 해충으로부터 보호받을 수 있다.
# 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.
#
# 한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다.
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로
# 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
# 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.
# 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.
#
# 1	1	0	0	0	0	0	0	0	0
# 0	1	0	0	0	0	0	0	0	0
# 0	0	0	0	1	0	0	0	0	0
# 0	0	0	0	1	0	0	0	0	0
# 0	0	1	1	0	0	0	1	1	1
# 0	0	0	0	1	0	0	1	1	1
# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해
# 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과
# 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다.
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.
#
# 출력
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.
import sys
# 파이썬의 기본 재귀는 1000으로 한정되어 있다.
# 재귀를 하다 에러가 난다면 아래와 같은 코드를 사용해서 해결한다.
sys.setrecursionlimit(10 ** 6)

# def dfs(x, y):
#     # 상좌하우의 방향
#     dx = [0, -1, 0, 1]
#     dy = [1, 0, -1, 0]
#
#     # 방향 탐색
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if (0 <= nx < m) and (0 <= ny < n):
#             if matrix[ny][nx] == 1:
#                 # 상하좌우에 값이 있으면 값을 0으로 변경한다.
#                 matrix[ny][nx] = 0
#                 dfs(nx, ny)
#     return
#
# # 테스트 케이스
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     m, n, k = map(int, sys.stdin.readline().split())
#     # 배추 위치쌍을 2차원 배열로 받기
#     matrix = [[0] * m for _ in range(n)]
#     # 흰지렁이수를 세기 위함
#     count = 0
#
#     # 배추 위치에 1삽입
#     for i in range(k):
#         x, y = map(int, sys.stdin.readline().split())
#         matrix[y][x] = 1
#
#     # 각 행과 열에서 값을 확인한다.
#     # 그리고 dfs 함수가 모두 끝나면 흰지렁이 수를 계산한다.
#     for i in range(m):
#         for j in range(n):
#             if matrix[j][i] == 1:
#                 dfs(i, j)
#                 count += 1
#
#     print(count)

import sys
from collections import deque

def bfs(x, y):
    deq = deque()
    deq.append((x, y))
    # 상좌하우의 방향
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    while deq:
        x, y = deq.popleft()
        # 방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < m) and (0 <= ny < n):
                if matrix[ny][nx] == 1:
                    deq.append((nx, ny))
                    # 상하좌우에 값이 있으면 값을 0으로 변경한다.
                    matrix[ny][nx] = 0
    return


# 테스트 케이스
t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    # 배추 위치쌍을 2차원 배열로 받기
    matrix = [[0] * m for _ in range(n)]
    # 흰지렁이수를 세기 위함
    count = 0

    # 배추 위치에 1삽입
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1

    # 각 행과 열에서 값을 확인한다.
    # 그리고 dfs 함수가 모두 끝나면 흰지렁이 수를 계산한다.
    for i in range(m):
        for j in range(n):
            if matrix[j][i] == 1:
                bfs(i, j)
                count += 1

    print(count)
