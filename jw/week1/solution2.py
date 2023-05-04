# 강의실배정
# https://www.acmicpc.net/problem/11000

# 해설 :
# RunTime :
# Memory :

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
