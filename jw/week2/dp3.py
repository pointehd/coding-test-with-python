# 제목 : 자두나무
# link : https://www.acmicpc.net/problem/2240
# 해설 : https://wooono.tistory.com/643
# 느낌 : 해설을 봐도 봐도 봐도 이해가 잘안된다 너무 어렵다
# RunTime : 72 ms
# Memory : 3,1256 KB


def solution1():
    t, w = map(int, input().split())
    tree = [0]
    for i in range(t):
        tree.append(int(input()))

    dp = [[0] * (w + 1) for _ in range(t + 1)]  # dp[7][2]

    for i in range(1, t + 1):
        if tree[i] == 1:
            dp[i][0] = dp[i - 1][0] + 1
        # 2번 나무에서 자두가 떨어진다면
        else:
            dp[i][0] = dp[i - 1][0]

        for j in range(1, w + 1):
            if tree[i] == 2 and j % 2 == 1:  #  현재 위치가 2일때  나무가 2번에서 떨어질때
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
            elif tree[i] == 1 and j % 2 == 0:  #  현재 위치가 1일때  나무가 1번에서 떨어질때
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
    print(max(dp[t]))


solution1()
