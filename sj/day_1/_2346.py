# 제목 : 풍선터트리기
# link : https://www.acmicpc.net/problem/2346
# 해설 : https://jobdong7757.tistory.com/117
# 느낌 : 갈길이 멀구나... 문제 자체는 어려운게 아닌데 LinkedList 이용해서 순회하게 하면 될꺼라 생각했는데 음.. 어렵네
# RunTime : 64 ms
# Memory : 3,4104 KB
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque(enumerate(map(int, input().split())))
result = []
while queue:
    idx, sum = queue.popleft()
    result += [idx + 1]

    if sum > 0:
        queue.rotate(-(sum - 1))
    elif sum < 0:
        queue.rotate(-sum)

print(*result)
