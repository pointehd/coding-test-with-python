# 제목 : 유기농 배추
# link : https://www.acmicpc.net/problem/1012
# 해설 :
# 느낌 : 맞았는데 시간이 너무 길다 ㅎ
# RunTime : 312 ms
# Memory : 31652 KB

import sys

sys.setrecursionlimit(10**6)  # 백준 재귀 한계 추가

testCaseCount = int(input())


def removeOne(array, width, height, maxWidth, maxHeight):
    if width < 0 or width >= maxWidth or height < 0 or height >= maxHeight:
        return
    if array[height][width] == 0:
        return
    array[height][width] = 0
    removeOne(array, width + 1, height, maxWidth, maxHeight)
    removeOne(array, width - 1, height, maxWidth, maxHeight)
    removeOne(array, width, height + 1, maxWidth, maxHeight)
    removeOne(array, width, height - 1, maxWidth, maxHeight)


for i in range(testCaseCount):
    result = 0
    X, Y, K = map(int, input().split())
    array = [[0] * X for _ in range(Y)]
    for j in range(K):
        w, d = map(int, input().split())
        array[d][w] = 1
    for j in range(Y):
        for k in range(X):
            if array[j][k] == 1:
                removeOne(array, k, j, X, Y)
                result += 1
    print(result)

##################################################################################################

# 해설 : 다른사람의 풀이
# 느낌 : dfs bfs 차이 인듯 큐를 이용한 bfs 로 풀면 시간이 줄어드네요? 일단 재귀는 사라진다  row, col 을 이용한 반복문도 배울점! 옛날에 했었는데 기억이 안났다.
# RunTime : 40 ms
# Memory : 30616 KB
num = int(sys.stdin.readline())

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs(x, y):
    queue = [(x, y)]
    matrix[x][y] = 0

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + row[i]
            ny = y + col[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0


for i in range(num):
    n, m, k = map(int, sys.stdin.readline().split())

    matrix = [[0] * m for i in range(n)]
    count = 0

    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        matrix[x][y] = 1

    for j in range(n):
        for k in range(m):
            if matrix[j][k] == 1:
                bfs(j, k)
                count += 1

    print(count)
