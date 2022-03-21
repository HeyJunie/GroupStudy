# 지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다.
# 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.
#
# 지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.
#
# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
# 큐에 처음에 포함되어 있던 수 N이 주어진다.
# 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.)
# 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

import sys

# 큐의 크기, 뽑아내려는 수의 개수
n, m = list(map(int, sys.stdin.readline().split()))
# 큐
que = [i for i in range(1, n + 1)]
# 뽑아내려는 수
pickNums = list(map(int, sys.stdin.readline().split()))
#연산 횟수
cnt = 0
# print(queue)

# 연산1 : 처음 오는 수를 뽑을 수 있다.
while pickNums:
    # 연산 조건 : 뽑으려는 수 큐의 앞쪽에 가깝나 뒤에 가깝나를 기준으로 한다.

    # 연산2 : 앞쪽에 가까우면 왼쪽으로 한 칸 이동
    if que.index(pickNums[0]) < len(que) - que.index(pickNums[0]):
        while True:
            # 만약 뽑아야 하는 수가 앞에 있으면 뽑음
            if que[0] == pickNums[0]:
                del que[0] # 큐에서 제거
                del pickNums[0] # 뽑아야 하는 수도 제거
                break
            # 연산2 수행
            else:
                que.append(que[0])
                del que[0]
                cnt +=1
    # 연산3 : 뒤쪽에 가까우면 오른쪽으로 한 칸 이동
    else:
        while True:
            # 만약 뽑아야 하는 수가 앞에 있으면 뽑음
            if que[0] == pickNums[0]:
                del que[0] # 큐에서 제거
                del pickNums[0] # 뽑아야 하는 수도 제거
                break
            # 연산2 수행
            else:
                que.insert(0, que[-1])
                del que[-1]
                cnt +=1

print(cnt)