# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.
import sys
from collections import deque

# dfs 함수
def dfs(v):
    # 방문한 곳에 1을 삽입
    visited1[v] = 1
    print(v, end=' ')
    # 재귀 함수 선언
    for i in range(1, n + 1):
        if visited1[i] == 0 and matrix[v][i] == 1:
            dfs(i)

# bfs 함수
def bfs(v):
    # 방문할 곳을 넣을 덱
    deq = deque()
    deq.append(v)
    # 방문한 곳에 1을 삽입
    visited2[v] = 1
    # 덱 안에 데이터가 없어질때까지 반복문 실행
    while deq:
        v = deq.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visited2[i] == 0 and matrix[v][i] == 1:
                deq.append(i)
                visited2[i] = 1

# n: 정점 갯수, m: 간선 갯수, v: 탐색을 시작할 정점 번호 입력 받기
n, m, v = map(int, sys.stdin.readline().rstrip().split())

# 배열은 0부터 시작하므로 n개의 수에 1을 더해 값들의 위치를 입력 받은 그대로 생각한다.
# n개의 숫자들 사이의 인접하는 0행렬을 생성
matrix = [[0] * (n + 1) for _ in range(n + 1)]
# 방문한 곳 확인을 위한 배열 생성
visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)

# 간선 갯수에 맞춰 두 개의 숫자들 입력 받기
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    # 입력 받은 두 값의 위치 체크를 위해 위치에 맞게 1 삽입
    matrix[a][b] = matrix[b][a] = 1

dfs(v)
print()
bfs(v)