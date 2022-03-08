# 행복 유치원 원장인 태양이는 어느 날 N명의 원생들을 키 순서대로 일렬로 줄 세우고, 총 K개의 조로 나누려고 한다.
# 각 조에는 원생이 적어도 한 명 있어야 하며, 같은 조에 속한 원생들은 서로 인접해 있어야 한다.
# 조별로 인원수가 같을 필요는 없다.
#
# 이렇게 나뉘어진 조들은 각자 단체 티셔츠를 맞추려고 한다.
# 조마다 티셔츠를 맞추는 비용은 조에서 가장 키가 큰 원생과 가장 키가 작은 원생의 키 차이만큼 든다.
# 최대한 비용을 아끼고 싶어 하는 태양이는 K개의 조에 대해 티셔츠 만드는 비용의 합을 최소로 하고 싶어한다.
# 태양이를 도와 최소의 비용을 구하자.

import sys

# 유치원에 있는 원생 수와 나누려고 하는 조의 개수
n, k = map(int, sys.stdin.readline().split())
# 입력받은 아이들의 키
kids = list(map(int, sys.stdin.readline().split()))

# 아이들의 키 차이 초기화하고,
# 키 차이를 최소화 하기 위해 차이를 정렬함
diff = []
for i in range(n-1) :
    diff.append(kids[i+1] - kids[i])
diff.sort()

cost = 0
for j in range(n-k):
    cost += diff[j]

print(cost)
