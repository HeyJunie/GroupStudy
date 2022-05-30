# 수열의 높이 조정

def solution(nums, m):
    answer = 0
    ch = [0] * 1001
    maxH = float('-inf')
    minH = float('inf')
    for x in nums:
        ch[x] += 1
        if x > maxH:
            maxH = x
        if x < minH:
            minH = x
    for i in range(m):
        if maxH == minH:
            return 0
        if ch[maxH] == 1:
            ch[maxH] -= 1
            maxH -= 1
            ch[maxH] += 1
        else:
            ch[maxH] -= 1
            ch[maxH - 1] += 1
        if ch[minH] == 1:
            ch[minH] -= 1
            minH += 1
            ch[minH] += 1
        else:
            ch[minH] -= 1
            ch[minH + 1] += 1

    answer = maxH - minH
    return answer

nums1 = [2, 1, 3, 7, 5]
m1 = 2

nums2 = [69, 42, 68, 76, 40, 87, 14, 65, 76, 81]
m2 = 50

nums3 = [3, 2, 3, 3, 4]
m3 = 0

print(solution(nums1, m1))
print(solution(nums2, m2))
print(solution(nums3, m3))

