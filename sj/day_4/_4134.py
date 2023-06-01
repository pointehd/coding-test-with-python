# 제목 : 다음 소수
# link : https://www.acmicpc.net/problem/4134
# 해설 :
# 느낌 :
# RunTime : 1516 ms
# Memory : 3,1256 KB

count = int(input())


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for _ in range(count):
    data = int(input())
    while True:
        if is_prime(data):
            print(data)
            break
        data += 1
