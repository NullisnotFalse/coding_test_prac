# 윤년
# https://www.acmicpc.net/problem/2753


# 조건문


# 풀이_1

# YEAR_1 = int(input())
YEAR_1 = 2000


def solution_1(YEAR_1):
    if YEAR_1 % 4 == 0:
        if YEAR_1 % 400 == 0:
            return 1
        elif YEAR_1 % 100 == 0:
            return 0
        else:
            return 1
    else:
        return 0


print(solution_1(YEAR_1))


# 풀이_2

# YEAR_2 = int(input())
YEAR_2 = 2000


def solution_2(YEAR_2):
    if YEAR_2 % 4 == 0 and YEAR_2 % 100 != 0 or YEAR_2 % 400 == 0:
        return 1
    else:
        return 0


print(solution_2(YEAR_2))


# 풀이_1은 실행 시간 44m / 풀이_2는 실행 시간 40m
