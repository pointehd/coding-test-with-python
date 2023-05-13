# 제목 : 지름길
# link : https://www.acmicpc.net/problem/1446
# 해설 : https://jinho-study.tistory.com/1014
# 느낌 : 흠 그래프는 아직 더봐야할것 같다 다음주는 실3 부터 다시와야지
# RunTime : 44 ms
# Memory : 3,1256 KB


def solution1():
    N, D = map(int, input().split())
    loads = [list(map(int, input().split())) for _ in range(N)]
    loads.sort(key=lambda load: load[0])
    dis = [i for i in range(D + 1)]

    for i in range(D + 1):
        if i > 0:
            dis[i] = min(dis[i], dis[i - 1] + 1)
        for s, e, d in loads:
            if s == i and e <= D and dis[i] + d < dis[e]:
                dis[e] = dis[i] + d

    print(dis[D])


solution1()
