# 제목 : 연결 요소의 개수
# link : https://www.acmicpc.net/problem/11724
# 해설 :
# 느낌 : 해설을 보긴 봤는데 내코드도 다 통과 했다...
# RunTime : 644 ms
# Memory : 65076 KB

## 이 아래 두줄 추가하면 내코드도 두개다 통과한다.. 무슨차이지
import sys

input = sys.stdin.readline


def solution1():
    N, M = map(int, input().split())
    nodes = [[] for _ in range(N + 1)]
    result = 0
    nodeCheck = [False for _ in range(N + 1)]

    def bfs(n):
        queue = []
        queue.append(n)
        nodeCheck[n] = True
        while queue:
            node = queue.pop()
            for num in nodes[node]:
                if not nodeCheck[num]:
                    nodeCheck[num] = True
                    queue.append(num)

    for i in range(M):
        s, e = map(int, input().split())
        nodes[s].append(e)
        nodes[e].append(s)

    for i in range(1, N + 1):
        if not nodeCheck[i]:
            bfs(i)
            result += 1
    print(result)


# 제목 : 연결 요소의 개수
# link : https://www.acmicpc.net/problem/11724
# 해설 :
# 느낌 : 해설을 보긴 봤는데 내코드도 다 통과 했다...
# RunTime : 776 ms
# Memory : 31256 KB
def solution2():
    N, M = map(int, input().split())
    node = [i for i in range(N + 1)]

    for i in range(M):
        s, e = map(int, input().split())
        minNum = min(node[s], node[e])
        maxNum = max(node[s], node[e])
        if minNum != maxNum:
            node[maxNum] = node[minNum]
            for j in range(1, N + 1):
                if node[j] == maxNum:
                    node[j] = node[minNum]

    print(len(set(node)) - 1)
