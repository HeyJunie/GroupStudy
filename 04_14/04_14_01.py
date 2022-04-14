# 상근이는 2차원 평면 위에서 움직일 수 있는 거북이 로봇을 하나 가지고 있다.
# 거북이 로봇에게 내릴 수 있는 명령은 다음과 같이 네가지가 있다.
#
# F: 한 눈금 앞으로
# B: 한 눈금 뒤로
# L: 왼쪽으로 90도 회전
# R: 오른쪽으로 90도 회전
#
# L과 R명령을 내렸을 때, 로봇은 이동하지 않고, 방향만 바꾼다.
# 명령을 나열한 것을 거북이 로봇의 컨트롤 프로그램이라고 한다.
#
# 상근이는 자신의 컨트롤 프로그램으로 거북이가 이동한 영역을 계산해보려고 한다.
# 거북이는 항상 x축과 y축에 평행한 방향으로만 이동한다.
# 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이를 구하는 프로그램을 작성하시오.
# 단, 직사각형의 모든 변은 x축이나 y축에 평행이어야 한다.
#
# 아래 그림에서 거북이는 가장 처음에 (0, 0)에 있고, 북쪽을 쳐다보고 있다.
# 컨트롤 프로그램이 FLFRFLBRBLB인 경우에 거북이는 아래와 같이 움직인다.
# 회색으로 빗금친 부분이 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형이다. 넓이는 4가 된다.
#
#
#
# 거북이가 지나간 영역이 직사각형을 만들지 않는 경우도 있다.
# 예를 들어, FFLLFF인 경우에 거북이는 y축의 위로만 지나다닌다.
# 이 경우에 거북이가 지나간 영역을 모두 포함하는 직사각형은 선분이고, 선분은 한 변이 0인 직사각형으로 생각할 수 있다.
# 따라서, 선분의 경우에 넓이는 0이 된다.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 컨트롤 프로그램이 주어진다.
# 프로그램은 항상 문제의 설명에 나와있는 네가지 명령으로만 이루어져 있고, 길이는 500을 넘지 않는다.
#
# 출력
# 각 테스트 케이스에 대해서, 거북이가 이동한 영역을 모두 포함하는 가장 작은 직사각형의 넓이를 출력한다.
import sys

# 테스트 케이스 입력
t = int(sys.stdin.readline())
# 이동 및 방향을 리스트에 담기
move = []
# 북서남동 -> 북(0, 1), 서(-1, 0), 남(0, -1), 동(1, 0)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 이동 및 방향 하나씩 입력 받기
for _ in range(t):
    move.append(list(map(str, sys.stdin.readline().strip())))

# move 리스트에서 리스트 하나씩 꺼내기
for idx in move:
    # 각 리스트의 x, y값들을 초기화
    x, y = 0, 0
    # 최대, 최소 값을 초기화
    max_x, max_y = 0, 0
    min_x, min_y = 0, 0
    # 방향 지시를 위함 - > 북0, 서1, 남2, 동3
    direction = 0
    # 리스트를 하나씩 뜯어서 생각하기
    for i in idx:
        # 만약 리스트 값들 중에 "F"가 있다면, 방향 지시에 맞춰 1칸 앞으로 이동
        if i == "F":
            x += dx[direction]
            y += dy[direction]

        # 만약 리스트 값들 중에 "B"가 있다면, 방향 지시에 맞춰 1칸 뒤로 이동
        elif i == "B":
            x -= dx[direction]
            y -= dy[direction]

        # 만약 리스트 값들 중에 "L"이 있다면, 방향을 하나씩 더해줌
        # 내가 방향을 북서남동 즉, 반시계 방향으로 설정했기 때문
        elif i == "L":
            if direction == 3:
                direction = 0
            else:
                direction += 1

        # 만약 리스트 값들 중에 "R"이 있다면, 방향을 하나씩 빼줌
        # 오른쪽으로 계속 방향을 바꾸면 시계방향임
        elif i == "R":
            if direction == 3:
                direction = 0
            else:
                direction -= 1

        # x, y의 최소값, 최대값을 각각 구함
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # 두번째 for문에서 빠져나와서 계산
    # 최대값과 최소값의 차이가 (-)가 될 수 있기 때문에 절대값을 씌워줌
    print(abs(max_x - min_x) * abs(max_y - min_y))
