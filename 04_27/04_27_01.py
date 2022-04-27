# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)
#
# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
#
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
# 값들을 담아줄 리스트
list = []

def dfs():
    # 리스트의 길이가 m인 숫자들을 출력한다.
    if len(list) == m:
        # 리스트 값이 '1', '2' ... 이런 형식이므로 join을 이용해 1 2 형식으로 바꿔줌
        print(' '.join(map(str, list)))
        return

    # 1부터 n까지의 숫자들로 반복문 실행
    for i in range(1, n+1):
        # 리스트에 i값을 넣어주고
        list.append(i)
        # 리스트 안의 숫자들을 출력해줌
        dfs()
        # 출력된 값들은 제거한다.
        list.pop()

dfs()