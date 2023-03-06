# 왕실의 나이트 p 115

input_data = input()

def solution(data) : 
    count = 0
    row = int(input_data[1])
    column = int(ord(input_data[0])) - int(ord('a')) + 1
    print(row, column)
    steps = [(-2, 1), (-2, -1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if next_row > 0 and next_row < 9 and next_column > 0 and next_column < 9:
            count += 1
    return count

print(solution(input_data))