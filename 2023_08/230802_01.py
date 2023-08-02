# 캐릭터의 좌표
# https://school.programmers.co.kr/learn/courses/30/lessons/120861


def direction(dir):
    if dir == "up":
        return [0, 1]
    elif dir == "down":
        return [0, -1]
    elif dir == "left":
        return [-1, 0]
    elif dir == "right":
        return [1, 0]


def solution(keyinput, board):
    answer = [0, 0]
    x_border = (board[0] - 1) / 2
    y_border = (board[1] - 1) / 2
    for dir in keyinput:
        key_input = direction(dir)
        temp = [x + y for x, y in zip(answer, key_input)]
        if x_border >= temp[0] >= -x_border and y_border >= temp[1] >= -y_border:
            answer = temp
    return answer
