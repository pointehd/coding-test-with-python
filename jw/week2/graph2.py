# 제목 : 완전 이진 트리
# link : https://www.acmicpc.net/problem/9934
# 해설 :
# 느낌 :
# RunTime : 40 ms
# Memory : 31256 KB


def solution1_recursive(arr: list, index: int, results: list):
    arrLength = len(arr)
    if arrLength > 1:
        center = arrLength // 2
        results[index].append(arr[center])
        solution1_recursive(arr[0:center], index + 1, results)
        solution1_recursive(arr[center + 1 : arrLength], index + 1, results)
    else:
        results[index].append(arr[0])


K = int(input())
trees = list(map(int, input().split()))
result = [[] for _ in range(K)]

solution1_recursive(trees, 0, result)
for i in range(K):
    print(*result[i])
