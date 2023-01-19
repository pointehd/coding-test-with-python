# 조건 n % 10 == 0 

coins = [500, 100, 50, 10]

def solution(n): # 내가 푼방식
    result = 0
    for coin in coins:
        result += int(n / coin)
        n %= coin
    return result

print(solution(1250))

# 책에서는 함수를 쓰지 않음.