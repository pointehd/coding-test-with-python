# 제목 : 쇠막대기
# link : https://www.acmicpc.net/problem/10799

from collections import deque


# 해설 :
# 느낌 :
# RunTime : 88 ms
# Memory : 3,4140 KB
def solution():
    inputs = deque(list(input()))
    stack = []
    last = ""
    result = 0

    tmp = inputs.popleft()
    last = tmp
    stack.append(tmp)
    result = 0

    while inputs:
        tmp = inputs.popleft()

        if tmp == "(":
            stack.append(tmp)
        else:
            stack.pop()
            if last == ")":
                result += 1
            else:
                result += len(stack)
        last = tmp
    print(result)


# 해설 : 맞힌사람 코드
# 느낌 : 풀이방식은 같지만 반복문 돌리는데 좀더 좋은것 같다.
# RunTime : 44 ms
# Memory : 31688 KB
def solution2():
    parentheses = input()
    stack = []
    cutting_count = 0

    for ele in parentheses:
        if ele == "(":
            stack.append(ele)
            last = ele
        else:
            stack.pop()
            if last == "(":
                cutting_count += len(stack)
                last = ele
            else:
                cutting_count += 1
    print(cutting_count)


solution2()
