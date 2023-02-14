def solution(prices: list):
    answer = 0
    minPrice = 1_000_000
    maxPrice = 0
    for price in prices:
        maxPrice = max(maxPrice, price)
        if minPrice > price:
            minPrice = price
            maxPrice = minPrice
        answer = max(answer, maxPrice - minPrice)
    return answer


print(solution([3, 2, 4, 8, 7]))
print(solution([3, 4, 1, 5, 4]))
