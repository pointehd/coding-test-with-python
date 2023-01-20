# 문제 : 큰 수의 법칙 (92p)
# 5 8 3 (배열의 크기 n , 사용횟수 m, 한 인덱스 연속 최대수 k)
# 2 4 5 6 7 (주어진 배열)

# TIL
# - 파이썬에서 입력받는 신기한 방법
# - 함수에서 전역 변수 값을 변경시 에러 발생

# 입력 받는법(input()) 입력
n, m, k = map(int, input().split())  # 신기하다.
arrays = list(
    map(int, input().split())
)  # 이건 더 신기 [map(int, input().split())] 이렇게 사용하면 [mapObject] 로 사용됨.
arrays.sort()  # 통합 내용

# version 1 : 내가 푼 방식
def solution1():
    count = m
    result = 0
    max = arrays[n - 1]
    secondMax = arrays[n - 2]

    while True:
        for i in range(k):
            if count == 0:
                break
            result += max
            count -= 1
        if count == 0:
            break
        result += secondMax
        count -= 1
    print("\n version 1) result :", result)
    print("=============END=============")


# version 2:
# 느낀점 : 답을 보고 이런 수학적 사고를 고려해서 리펙토링을 해야하나 생각했는데
#          짜다보니 이정도 사고는 할수 있는게 맞다고 생각된다.
def solution2():
    result = 0
    max = arrays[n - 1]
    secondMax = arrays[n - 2]

    maxCount = int(m / k) * k
    secondCount = m - maxCount

    result = max * maxCount + secondMax * secondCount
    print("\n version 2) result :", result)
    print("=============END=============")


# use funtion()
solution1()
solution2()
