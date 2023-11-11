# 직사각형 넓이 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120860


# 풀이_01 -> 집합과 정렬 사용


def solution_01(dots):
    x_list = sorted(set([dots[0][0], dots[1][0], dots[2][0], dots[3][0]]))
    y_list = sorted(set([dots[0][1], dots[1][1], dots[2][1], dots[3][1]]))
    answer = (x_list[1] - x_list[0]) * (y_list[1] - y_list[0])
    return answer


# 풀이_02 -> 정렬만 사용


def solution_02(dots):
    dots.sort()
    answer = (dots[-1][0] - dots[0][0]) * (dots[1][1] - dots[0][1])
    return answer
