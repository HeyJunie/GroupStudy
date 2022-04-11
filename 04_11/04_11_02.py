# 홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.
#
# 9	2	3
# 8	1	4
# 7	6	5
#
# 25	10	11	12	13
# 24	9	2	3	14
# 23	8	1	4	15
# 22	7	6	5	16
# 21	20	19	18	17
# N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오.
# 또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오. 예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.
#
# 입력
# 첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다. 둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.
#
# 출력
# N개의 줄에 걸쳐 표를 출력한다. 각 줄에 N개의 자연수를 한 칸씩 띄어서 출력하면 되며, 자릿수를 맞출 필요가 없다.
# N+1번째 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력한다.

######################### 런타임 에러 ########################
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
board = [[0 for _ in range(n)]for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

row = n//2
col = n//2
num = 1
len = 0
board[row][col] = num

while True:
    for i in range(4):
        for _ in range(len):
            row += dr[i]
            col += dc[i]
            num += 1
            board[row][col] = num
            if num == m:
                result = [row+1, col+1]

    if row == 0 and col == 0:
        break
    row -= 1
    col -= 1
    len += 2

for i in range(n):
    print(*board[i])
print(*result)