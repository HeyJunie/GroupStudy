# 한상덕은 이번에 중덕 고등학교에 새로 부임한 교장 선생님이다.
# 교장 선생님으로서 첫 번째 일은 각 반의 수학 시험 성적의 통계를 내는 일이다.
# 중덕 고등학교 각 반의 학생들의 수학 시험 성적이 주어졌을 때,
# 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.

x = int(input())

for i in range(1, x+1) :

    n_score = list(map(int, input().split()))
    n = int(n_score[0])
    score = n_score[1:]
    score.sort(reverse=True)

    diff = 0
    for j in range(len(score) - 1) :
        diff = max(diff, score[j] - score[j+1])


    print('Class {}'.format(i))
    print('Max {}, Min {}, Largest gap {}'.format(score[0], score[-1], diff))