# 시각 p 113
# 쉬운 문제여서 풀지 않을까 하다가 파이썬을 익히기 위해 작성.

n = int(input())


def solution(n: int):
    count = 0
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                if "3" in str(i) + str(j) + str(k):
                    count += 1
    return count


print(solution(n))
