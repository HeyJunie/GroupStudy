# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다.
# ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다.
# 자연수 x가 주어졌을 때,
# ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

import time
start = time.time() # 시작시간 저장
import sys

# 테스트 케이스 개수 -> t
t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for i in range(t) :
    # 연종이 본 정수 개수 -> n
    n = int(sys.stdin.readline())
    # 연종이 본 정수들 -> note1
    note1 = set(map(int, sys.stdin.readline().split()))
    # 동규가 받아 적은 정수 개수 -> m
    m = int(sys.stdin.readline())
    # 동규가 받아 적은 정수들 -> note2
    note2 = list(map(int, sys.stdin.readline().split()))

    # note2 정수를 보면서 note1과 비교 반복
    for number in note2 :
        if number in note1 :
            print(1)
        else :
            print(0)


print(f"측정된 시간 : {time.time() - start}") # 단위는 초