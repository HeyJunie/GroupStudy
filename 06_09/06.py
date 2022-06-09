# 가격 책정

def getAverage(prices, a, b):
    sum = 0
    for i in range(a, b + 1):
        sum += prices[i]
    avg = sum // (b - a + 1)
    return avg


def solution(prices, d, k):
    prices.sort()
    n = len(prices)
    if prices[n - 1] - prices[0] <= d:
        return getAverage(prices, 0, n - 1)
    elif prices[n - 2] - prices[1] <= d:
        return getAverage(prices, 1, n - 2)

    for i in range(n - k + 1):
        if prices[i + k - 1] - prices[i] <= d:
            return getAverage(prices, i, i + k - 1)
    return prices[(n - 1) // 2]  # 어차피 인덱스 0번부터 시작하고 오름차순 정렬이므로


print(solution([4, 5, 6, 7, 8], 4, 3))
print(solution([4, 5, 6, 7, 8], 2, 3))
print(solution([4, 5, 6, 7, 8], 1, 2))
print(solution([8, 4, 5, 7, 6], 1, 3))
print(solution([1, 8, 1, 8, 1, 8], 6, 4))