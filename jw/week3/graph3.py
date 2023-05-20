# 제목 : DFS 와 BFS
# link : https://www.acmicpc.net/problem/1260
# 해설 :
# 느낌 :
# RunTime : 76 ms
# Memory : 34184 KB
import sys
from collections import deque

input = sys.stdin.readline


N, M, V = map(int, input().split())
nodes = [[] for _ in range(N + 1)]
dfsCheck = [False] * (N + 1)
dfsResult = []
bfsCheck = [False] * (N + 1)
bfsResult = []


def dfs(nodes, v):
    dfsCheck[v] = True
    dfsResult.append(v)
    for value in nodes[v]:
        if not dfsCheck[value]:
            dfs(nodes, value)


def bfs(nodes, v):
    queue = deque([v])
    bfsCheck[v] = True
    while queue:
        data = queue.popleft()
        bfsResult.append(data)
        for node in nodes[data]:
            if not bfsCheck[node]:
                bfsCheck[node] = True
                queue.append(node)


for _ in range(M):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)
sorted_nodes = [sorted(sublist) for sublist in nodes]

dfs(sorted_nodes, V)
bfs(sorted_nodes, V)
print(*dfsResult)
print(*bfsResult)
