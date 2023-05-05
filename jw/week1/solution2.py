import heapq

# 강의실배정
# https://www.acmicpc.net/problem/11000


# 해설 :
# RunTime :
# Memory : 메모리  초과
def solution1():
    n = int(input())
    study = {}
    for i in range(n):
        x, y = map(int, input().split())
        for j in range(x, y):
            if study.get(j) is None:
                study[j] = 1
            else:
                study[j] += 1
    print(max(study, key=study.get))


# solution1()


# 해설 : https://hongcoding.tistory.com/79
# ?? 아니 답을 봐도 안되면 어쩌자규 ...
# RunTime : 시간초과
# Memory :
def solution2():
    n = int(input())
    study = []
    for i in range(n):
        start, end = map(int, input().split())
        study.append([start, end])
    sorted(study, key=lambda x: x[0])

    room = []
    heapq.heappush(room, study[0][1])

    for i in range(1, n):
        if study[i][0] < room[0]:
            heapq.heappush(room, study[i][1])
        else:
            heapq.heappop(room)
            heapq.heappush(room, study[i][1])
    print(len(room))


solution2()
