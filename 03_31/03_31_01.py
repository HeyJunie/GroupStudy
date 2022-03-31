# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
#
# 명령은 총 여덟 가지이다.
#
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque

# 명령의 수
n = int(sys.stdin.readline())

# 명령어 함수 처리
def push_front(x, deq):
    deq.appendleft(x)
    return deq

def push_back(x, deq):
    deq.append(x)
    return deq

def pop_front(deq):
    if deq:
        print(deq.popleft())
    else:
        print(-1)

def pop_back(deq):
    if deq:
        print(deq.pop())
    else:
        print(-1)

def size(deq):
    print(len(deq))

def empty(deq):
    if deq:
        print(0)
    else:
        print(1)

def front(deq):
    if deq:
        print(deq[0])
    else:
        print(-1)

def back(deq):
    if deq:
        print(deq[-1])
    else:
        print(-1)

# 명령어 사전
order_dict = {
    'push_front' : push_front,
    'push_back' : push_back,
    'pop_front' : pop_front,
    'pop_back' : pop_back,
    'size' : size,
    'empty' : empty,
    'front' : front,
    'back' : back
}

# 명령어 처리
deq = deque()

for _ in range(n):
    # push_back과 push_front는 띄어쓰기 후에 값을 더 받아옴
    # 명령을 리스트 형태로 받아오는 것
    order = sys.stdin.readline().split()
    # order[0]=명령어, order[1]=정수
    cmd = order[0]


    if len(order) == 1:
        # pop_front, pop_back, size, empty,front, back
        order_dict[cmd](deq)
    else:
        # push_front, push_back -> 이 둘은 값을 입력도 해줘야 함.
        x = int(order[1])
        deq = order_dict[cmd](x, deq)