def solution(nums):
    counter = {}

    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    results = []
    for key, value in counter.items():
        if value == 1:
            results.append(key)

    if not results:
        return -1

    results = sorted(results)

    return results[-1]

nums1 = [5, 7, 3, 9, 4, 9, 8, 3, 1]
print(solution(nums1))