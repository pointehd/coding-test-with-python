# 상하좌우 
# if~elif 를 사용하려 했지만 책의 방법이 신박해서 따라해봄. 2중 반복문이지만 switch 문을 이용하여 하는 것 보다 깔끔한 것 같기도 하고 애매함.
n = int(input())
inputs = input().split()

def solution(size, commands):
    types = ['L', 'R', 'U', 'D']
    # [L, R, U, D] command
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    x, y = 1, 1
    for command in commands:
        for i in range(len(types)):
            if(types[i] == command):
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > size or ny > size:
            continue
        x, y = nx, ny
    return [x, y]


print(solution(n, inputs))
