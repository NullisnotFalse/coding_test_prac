# https://school.programmers.co.kr/learn/courses/30/lessons/120847


# 정렬을 사용한 방법
def solution_01(numbers):
    temp_list = sorted(numbers)
    answer = temp_list[-1] * temp_list[-2]
    return answer


# 조합을 사용한 방법
import itertools


def solution_02(numbers):
    comb = list(itertools.combinations(numbers, 2))
    answer = 0
    for i1, i2 in comb:
        if i1 * i2 > answer:
            answer = i1 * i2
    return answer
