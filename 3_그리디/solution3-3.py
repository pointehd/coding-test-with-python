n, m = map(int, input().split())
cardMap = []
for i in range(n):
    cardList = list(map(int, input().split()))
    cardMap.append(cardList)


def solution1(cardsList: list):
    result = 0
    for cards in cardList:
        minLine = list(filter(lambda card: card >= result, cardList))
        result = max(min(minLine), result)
    return result


print(solution1(cardMap))


# 책에서는 한줄 입력받으며 답을 구했지만 나는 정리 목적도 있기 때문에 위와 같이 분리하여 구현
# 내가 푼방법과 책과 큰차이 없음.
