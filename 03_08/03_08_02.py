# 하나의 양팔 저울을 이용하여 물건의 무게를 측정하려고 한다.
# 이 저울의 양 팔의 끝에는 물건이나 추를 올려놓는 접시가 달려 있고, 양팔의 길이는 같다.
# 또한, 저울의 한쪽에는 저울추들만 놓을 수 있고, 다른 쪽에는 무게를 측정하려는 물건만 올려놓을 수 있다.
#
# 무게가 양의 정수인 N개의 저울추가 주어질 때,
# 이 추들을 사용하여 측정할 수 없는 양의 정수 무게 중 최솟값을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 무게가 각각 3, 1, 6, 2, 7, 30, 1인 7개의 저울추가 주어졌을 때,
# 이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값은 21이다.

import sys

# 저울추 개수
n = int(sys.stdin.readline())
# 저울추 무게
wt = list(map(int,sys.stdin.readline().split()))
wt.sort()

# 저울추 합
sumWt = 0
# 측정할 수 없는 무게 최소값
minWt = 0
for i in range(n) :
    if sumWt+1 >= wt[i] :
        sumWt += wt[i]

    else :
        break

minWt = sumWt + 1
print(minWt)