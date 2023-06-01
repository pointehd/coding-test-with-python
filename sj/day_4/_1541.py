# 제목 : 잃어버린 괄호
# link : https://www.acmicpc.net/problem/1541
# 해설 :
# 느낌 :
# RunTime : 40 ms
# Memory : 31256 KB


dataStr = input()
tmp = ""
operator = ""
datas = []
for i in dataStr:
    if i == "+" or i == "-":
        datas.append(int(operator + tmp))
        tmp = ""
        operator = i
    else:
        tmp += i

datas.append(int(operator + tmp))

sumResult = 0
minusStack = []
for i in datas:
    if i < 0:
        if len(minusStack) == 0:
            minusStack.append(-i)
        else:
            sumResult -= sum(minusStack)
            minusStack = []
            minusStack.append(-i)
    else:
        if len(minusStack) == 0:
            sumResult += i
        else:
            minusStack.append(i)
sumResult -= sum(minusStack)

print(sumResult)


# 해설 :다른사람 풀이
# 느낌 : 진짜 미췄다
# RunTime : 32 ms
# Memory : 30616 KB
def solution():
    exp = input().split("-")
    num = []
    for i in exp:
        cnt = 0
        sum = i.split("+")
        for j in sum:
            cnt += int(j)
        num.append(cnt)
    ans = num[0]
    for i in range(1, len(num)):
        ans -= num[i]
    print(ans)
