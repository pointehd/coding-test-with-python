# 제목 : 카드 구매하기
# link : https://www.acmicpc.net/problem/11052
# 해설 : https://infinitt.tistory.com/250
# 느낌 : 아 거의 다왔었는데 답을 봐버렸음. ㅠㅠ 이걸 dp인걸 알고 풀어도 이정도인데 모르고 풀면 어케풀지..
# RunTime :  216 ms
# Memory : 3,1256 KB
def solution1():
    n = int(input())
    pays = list(map(int, input().split()))
    pays.insert(0, 0)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i - j] + pays[j])
    print(dp[n])


solution1()
