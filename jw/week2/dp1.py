# 제목 : 2*n 타일링
# link : https://www.acmicpc.net/problem/11726
# 해설 : X
# 느낌 :
# RunTime :  44 ms
# Memory :  3,1388 KB
def solution1():
    n = int(input())
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n] % 10_007)


solution1()
