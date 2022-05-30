# 빈도수 구하기

import collections, operator
def solution(nums, k):
    answer=[]
    nH=collections.defaultdict(int)
    for x in nums:
        nH[x]+=1
    tmp=sorted(nH.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(k):
        answer.append(tmp[i][0])
    return answer

nums1, k1 = [1, 1, 1, 2, 2, 3], 2
nums2, k2 = [3, 3, 3, 5, 1, 1, 1, 7, 2, 2], 3

print(solution(nums1, k1))
print(solution(nums2, k2))