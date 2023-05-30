# 제목 : 트리의 부모찾기
# link : https://www.acmicpc.net/problem/11725
# 해설 :
# 느낌 : 코드에 다른사람 코드 보고 배울점 적음.
# RunTime : 292 ms
# Memory : 5,0772 KB
import sys

input = sys.stdin.readline

nodeCount = int(input())


node = [[] for _ in range(nodeCount + 1)]
visited = [False] * (nodeCount + 1)
result = [0] * (nodeCount + 1)

for _ in range(nodeCount - 1):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)


def findOneBfs():
    startNode = 1
    stack = []
    visited[startNode] = True
    stack.append(startNode)
    while stack:
        now = stack.pop()
        for n in node[now]:
            if not visited[n]:  # visited 말고 result 로 해도된다!
                stack.append(n)
                result[n] = now
                visited[n] = True


findOneBfs()

for n in result[2:]:
    print(n)
# print(*parents[2:], sep="\n") # 이런방법도 있다 출력할때
