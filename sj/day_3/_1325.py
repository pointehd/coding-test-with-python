# 제목 : 효율적인 해킹
# link : https://www.acmicpc.net/problem/1325
# 해설 : 내가 풀고 시간초과 때문에 답을 봤는데 다똑같이 풀었는데 이상하다..ㅠㅠ
# 느낌 : 뭔가 더 효율적으로 풀수 있을것 같은데 코드가 안짜지네 ...
# RunTime : 1,2588 ms
# Memory : 20,8976 KB
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

node = [[] for _ in range(N + 1)]

for i in range(M):
    s, e = map(int, input().split())
    node[e].append(s)

result = []
maxCount = 0

countNode = [0] * (N + 1)


def dfs(startNode):
    checkNode = [False] * (N + 1)
    checkNode[startNode] = True
    queue = [startNode]
    count = 1
    while queue:
        value = queue.pop()
        for n in node[value]:
            if countNode[startNode] != 0:
                return count + countNode[startNode]
            if not checkNode[n]:
                count += 1
                queue.append(n)
                checkNode[n] = True
    return count


for i in range(1, N + 1):
    countNode[i] = dfs(i)
    v = countNode[i]
    if maxCount < v:
        result = [i]
        maxCount = v
    elif maxCount == v:
        result.append(i)

print(*result)
