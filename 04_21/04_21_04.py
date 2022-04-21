# 문제
# 정수는 정수로 이루어진 리스트로 재미있는 놀이를 하려고 한다.
#
# 리스트에서 연속된 N개의 값 중 최대값, 최소값을 구한다. 이 값이 각각 원래 리스트의 최대값, 최소값과 같게 하려고 한다.
#
# 이를 만족하는 N 중 가장 작은 수를 반환하는 함수를 작성하시오.
#
# 입력 설명
# 정수로 이루어진 길이가 100000 이하인 리스트
#
# 출력 설명
# 조건을 만족하는 부분 리스트의 길이
#
# 입력 예시
# [4, 6, 8, 1, 0, 9, 3, 4, 7, 3]
#
# 출력 예시
# 2
def solution(nums):
    num_list = []
    num_list.append(min(nums))
    num_list.append(max(nums))

    for i in range(len(nums)):
        for j in range(len(nums)):
            if num_list[0] == nums[i] and num_list[1] == nums[j]:
                answer = j-i+1
    return answer

nums = [4, 6, 8, 1, 0, 9, 3, 4, 7, 3]
print(solution(nums))
