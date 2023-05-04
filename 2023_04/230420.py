# https://school.programmers.co.kr/learn/courses/30/lessons/120821


def solution_01(num_list):
    answer = num_list[::-1]
    return answer


def solution_02(num_list):
    num_list.reverse()
    return num_list


def solution_03(num_list):
    answer = list(reversed(num_list))
    return answer


import numpy as np


def solution_04(num_list):
    answer = np.flip(np.array(num_list)).tolist()
    return answer


def solution_05(num_list):
    answer = np.flipud(np.array(num_list)).tolist()
    return answer
