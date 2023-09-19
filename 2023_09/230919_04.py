# 사분면 고르기
# https://www.acmicpc.net/problem/14681


# 조건문


# 풀이_1

# x_1 = int(input())
# y_1 = int(input())
x_1 = 12
y_1 = 5


def solution_1(x_1, y_1):
    if x_1 > 0:
        if y_1 > 0:
            return 1
        elif y_1 < 0:
            return 4
    elif x_1 < 0:
        if y_1 > 0:
            return 2
        elif y_1 < 0:
            return 3


print(solution_1(x_1, y_1))


# 풀이_2

# x_2 = int(input())
# y_2 = int(input())
x_2 = 12
y_2 = 5


def solution_2(x_2, y_2):
    if x_2 > 0 and y_2 > 0:
        return 1
    elif x_2 < 0 and y_2 > 0:
        return 2
    elif x_2 < 0 and y_2 < 0:
        return 3
    elif x_2 > 0 and y_2 < 0:
        return 4


print(solution_2(x_2, y_2))


# 풀이_1, 풀이_2 모두 실행 시간은 40m
