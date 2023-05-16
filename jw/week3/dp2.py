# 제목 : 1로 만들기 2
# link : https://www.acmicpc.net/problem/12852
# 해설 :
# 느낌 : 음.. 통과는 했는데 시간이 많이 나와 찝찝하다 다른사람 코드도 봤는데 대단하다
# RunTime : 1420 ms
# Memory : 30,7792 KB
def solution():
    N = int(input())
    dp = [[] for _ in range(N + 1)]
    dp[1].append(1)

    for i in range(2, N + 1):
        dp[i].append(i)
        tmp = []
        if i % 2 == 0:
            tmp = dp[i // 2]
        if i % 3 == 0:
            if len(tmp) == 0 or len(tmp) > len(dp[i // 3]):
                tmp = dp[i // 3]
        if len(tmp) == 0 or len(tmp) > len(dp[i - 1]):
            tmp = dp[i - 1]
        dp[i].extend(tmp)

    print(len(dp[N]) - 1)
    print(*dp[N])


# 해설 :
# 느낌 : 어마어마 하게 똑똑한듯... 메모리랑 시간차이가 미쳤다.
# RunTime : 44 ms
# Memory : 3,1256 KB
def solution2():
    X = int(input())
    q = [X]
    vst = {X: -1}

    for x in q:
        if x == 1:
            break
        t = [x - 1]
        if x % 2 == 0:
            t.append(x // 2)
        if x % 3 == 0:
            t.append(x // 3)
        for y in t:
            if y > 0 and y not in vst:
                vst[y] = x
                q.append(y)
    Q = 1
    ans = []
    while Q > 0:
        ans.append(Q)
        Q = vst[Q]

    print(len(ans) - 1)
    print(*ans[::-1])


solution()
