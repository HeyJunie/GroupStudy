# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다.
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다.
# 단, N은 홀수라고 가정하자.
#
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
import sys

n = int(sys.stdin.readline())

nums = []
for i in range(n) :
    nums.append(int(sys.stdin.readline()))

# 1. 산술평균
mean= round((sum(nums) / n))
print(mean)

# 2. 중앙값
nums.sort()
median = nums[round(n/2)]
print(median)

# 3. 최빈값
# 딕셔너리 이용
cnt_dict = {}
for i in nums :

    if i in cnt_dict :
        cnt_dict[i] += 1
    else :
        cnt_dict[i] = 1

max_cnt = max(cnt_dict.values())
frequency = []
for i in cnt_dict :
    if max_cnt == cnt_dict[i] :
        frequency.append(i)

if len(frequency) > 1 :
    frequency.sort()
    print(frequency[1])
else :
    print(frequency[0])

# 4. 범위
rang = abs(nums[-1] - nums[0])
print(rang)