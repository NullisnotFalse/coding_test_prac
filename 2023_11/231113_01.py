# OX퀴즈
# https://school.programmers.co.kr/learn/courses/30/lessons/120907


# 풀이_01 -> eval(), split() 사용


def solution_01(quiz):
    answer = []
    for modi in quiz:
        left, right = modi.split(" = ")
        if eval(left) == int(right):
            answer.append("O")
        else:
            answer.append("X")
    return answer


# 풀이_02 -> eval()을 사용하지 않는 방법


def solution_02(quiz):
    answer = []
    for modi in quiz:
        left, z = modi.split(" = ")
        x, oper, y = left.split()
        if oper == "+" and int(x) + int(y) == int(z):
            answer.append("O")
        elif oper == "-" and int(x) - int(y) == int(z):
            answer.append("O")
        else:
            answer.append("X")
    return answer


# 풀이_02가 실행시간이 더 빠름
