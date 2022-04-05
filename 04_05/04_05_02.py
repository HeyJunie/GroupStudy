# 문제
# N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다.
# 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오.
# 이때, 정사각형은 행 또는 열에 평행해야 한다.
#
# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.
#
# 출력
# 첫째 줄에 정답 정사각형의 크기를 출력한다.
import sys
# N x M 값 입력
n, m = map(int, sys.stdin.readline().split())
# 사각형 꼭짓점들의 값 입력
rect = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
# N과 M 값에서 최솟값을 기준으로 정사각형이 최대가 될 수 있음
d = min(n, m)
# 정사각형의 최대값은 1부터 시작
max_size = 1

# i번째에서
for i in range(n):
    # j번째에서
    for j in range(m):
        # n, m 최솟값 중 최대 크기의 정사각형을 찾기 위해
        for k in range(d):
            # 만약 [i][j]번째의 값과 [i-k][j]번째 값과 [i][j-k]번째 값이 같다면
            # 가장 큰 정사각형을 찾을 수 있다.
            if ((i + k) < n) and ((j + k) < m) and (rect[i][j] == rect[i][j + k] == rect[i + k][j] == rect[i + k][j + k]):
                # k 값으로 생각했더니, 값이 전부 1씩 작게 나옴..
                max_size = max(max_size, (k+1)**2)

print(max_size)