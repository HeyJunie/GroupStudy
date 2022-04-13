# 문제
# 상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.
#
# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다.
# 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다.
# 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
#
# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)
#
# 다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
#
# 사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.
#
# 출력
# 첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.
import sys

# nxn 보드 크기 입력
n = int(sys.stdin.readline())
# 사탕 집어넣을 리스트
candies = []
# 먹을 사탕 갯수 값 초기화
candy_cnt = 1

# 사탕 색별 리스트에 담기
for _ in range(n):
    candies.append(list(map(str, sys.stdin.readline())))

# 행의 사탕들 확인
def row_check():
    global candy_cnt
    # 2차원 리스트 안의 값을 하나하나 비교
    for i in range(n):
        row_count = 1 # 행 사탕 갯수 세기
        for j in range(n-1):
            # 행 값들을 비교
            if candies[i][j] == candies[i][j+1]:
                row_count += 1
                # 상근이가 먹을 사탕 갯수는 최대 갯수
                candy_cnt = max(row_count, candy_cnt)
            else:
                row_count = 1 # 이거 안하면 틀림.....

# 열의 사탕들 확인
def col_check():
    global candy_cnt
    # 2차원 리스트 안의 값을 하나하나 비교
    for i in range(n):
        col_count = 1 # 열 사탕 갯수 세기
        for j in range(n-1):
            # 열 값들을 비교
            if candies[j][i] == candies[j+1][i]:
                col_count += 1
                # 상근이가 먹을 사탕 갯수는 최대 갯수
                candy_cnt = max(col_count, candy_cnt)
            else:
                col_count = 1 # 이거 안하면 틀림.....

# 사탕 근접 위치 이동
for i in range(n):
    for j in range(n-1):
        # 만약 행 사이에서 근접 사탕 색이 다르다면
        if candies[i][j] != candies[i][j+1]:
            # 행 근접 위치 교환
            candies[i][j], candies[i][j+1] = candies[i][j + 1], candies[i][j]
            # 행 체크 -> 갯수 세고
            row_check()
            # 열 체크 -> 갯수 세고
            col_check()
            # 다시 제자리로 돌려놓음 -> 다시 안돌려놓으면 안됨!!
            candies[i][j+1], candies[i][j] = candies[i][j], candies[i][j+1]

        # 만약 열 사이에서 근접 사탕 색이 다르다면
        if candies[j][i] != candies[j+1][i]:
            # 행 근접 위치 교환
            candies[j][i], candies[j+1][i] = candies[j+1][i], candies[j][i]
            # 행 체크 -> 갯수 세고
            row_check()
            # 열 체크 -> 갯수 세고
            col_check()
            # 다시 제자리로 돌려놓음 -> 다시 안돌려놓으면 안됨!!
            candies[j+1][i], candies[j][i] = candies[j][i], candies[j+1][i]

print(candy_cnt)