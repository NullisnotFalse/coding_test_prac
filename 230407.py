# https://school.programmers.co.kr/learn/courses/30/lessons/120956


import itertools


def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    baby_babbling = []
    for i in range(1, 5):
        for j in itertools.permutations(baby, i):
            baby_babbling.append(("").join(j))
    for i in baby_babbling:
        for j in babbling:
            if i == j:
                answer += 1
    return answer
