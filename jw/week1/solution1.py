# 제곱수의 합
# https://www.acmicpc.net/problem/1699

# 해설 : https://lakelouise.tistory.com/61
# RunTime : 4784 ms
# Memory : 3,5108 KB

n = int(input())

dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if j * j > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
# print(dp)

print(dp[n])


# ==================


# 해설 :
# RunTime : 시간초과
# Memory :
n = int(input())

dp = [i for i in range(n + 1)]

tmp = 1
while tmp**2 < n + 1:
    dp[tmp**2] = 1
    tmp += 1

for i in range(1, n + 1):
    for j in range(1, i // 2 + 1):
        if dp[i] == 1:
            break
        dp[i] = min(dp[i], dp[i - j] + dp[j])

print(dp[n])
