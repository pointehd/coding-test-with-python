# TIL
# - // 연산은 몫을 가져옴
# - ** 거듭제곱

n, k = map(int, input().split())


# version 1 : 내가 푼 방식
def solution1(n1):
    result = 0
    while n1 != 1:
        result += 1
        if n1 % k == 0:
            n1 /= k
        else:
            n1 -= 1
    return result


print(solution1(n))


# solution  : 해설 보고 푼방식
# 느낀점 :지렸다... 어떻게 이런 생각을.. 반복 수 줄이기!!
def solution2(n1):
    result = 0
    while True:
        target = (n1 // k) * k
        result += n1 - target
        n1 = target
        if n1 < k:
            break
        result += 1
        n1 //= k
    return result + n1 - 1


print(solution2(n))
