# 제목 : 바이러스
# link : https://www.acmicpc.net/problem/2606
# 해설 :
# 느낌 :
# RunTime : 40 ms
# Memory : 3,1256 KB
import sys

input = sys.stdin.readline

comCount = int(input())
nodeCount = int(input())
network = [[] for _ in range(comCount + 1)]
visited = [True] * (comCount + 1)

for _ in range(nodeCount):
    s, e = map(int, input().split())
    network[s].append(e)
    network[e].append(s)


def bfs(start):
    result = 0
    task = []
    visited[start] = False
    task.append(start)
    while task:
        n = task.pop()
        for i in network[n]:
            if visited[i]:
                visited[i] = False
                task.append(i)
                result += 1
    return result


print(bfs(1))
