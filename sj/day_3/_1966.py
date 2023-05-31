# 제목 : 프린터 큐
# link : https://www.acmicpc.net/problem/1966
# 해설 :
# 느낌 : 우선순위 큐로하다가 오래걸림 문제를 똑바로 읽을것!
# RunTime : 76 ms
# Memory : 3,4120 KB
import sys
from collections import deque

input = sys.stdin.readline

testCount = int(input())

finder = []
datas = []
for i in range(testCount):
    _, find = map(int, input().split())
    data = deque(list(map(int, input().split())))

    result = 0
    while data:
        maxNum = max(data)
        left = data.popleft()
        find -= 1
        if maxNum == left:
            result += 1
            if find < 0:
                print(result)
                break
        else:
            data.append(left)
            if find < 0:
                find = len(data) - 1
