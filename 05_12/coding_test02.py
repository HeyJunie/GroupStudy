from collections import deque
def solution(width, height, start_x, start_y, end_x, end_y, obstacles):
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    chess = [[0] * width for _ in range(height)]

    for i in range(len(obstacles)):
        for j in range(2):
            chess[obstacles[i][0]][obstacles[i][1]] = 1

    queue = deque([[start_x, start_y]])
    if start_x==end_x and start_y==end_y:
        return 0
    while queue and not chess[end_x][end_y]:
        x, y = queue.popleft()
        for i,j in zip(dx,dy):
            nx = x + i
            ny = y + j
            if 0 <= nx < width and 0 <= ny < height:
                if not chess[nx][ny]:
                    chess[nx][ny] = chess[x][y]+1
                    queue.append([nx, ny])
    return chess[end_x][end_y]


width = 10
height = 10
start_x = 2
start_y = 5
end_x = 8
end_y = 9
obstacles = [[1, 2], [5, 3], [0, 9], [0, 4]]

print(solution(width, height, start_x, start_y, end_x, end_y, obstacles))