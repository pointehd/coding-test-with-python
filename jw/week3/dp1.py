# 제목 : 이친수
# link : https://www.acmicpc.net/problem/2193
# 해설 :
# 느낌 : EZ!
# RunTime : 52 ms
# Memory : 31256 KB


N = int(input())

dp = [0] * (N + 1)
dp[0], dp[1] = 0, 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[N])
