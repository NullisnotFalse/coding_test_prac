# https://school.programmers.co.kr/learn/courses/30/lessons/120809


import numpy as np


# 지연시간 더 길었음
def solution_01(numbers):
    answer = (np.array(numbers) * 2).tolist()
    return answer


# 지연시간 더 짧았음
def solution_02(numbers):
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer
