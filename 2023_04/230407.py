# https://school.programmers.co.kr/learn/courses/30/lessons/120956


import itertools


def solution_01(babbling):
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


def solution_02(babbling):
    answer = 0
    check = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in check:
            i = i.replace(j, " ", 1)  # babbling에서 주어진 단어를 공백처리
        if i.isspace():  # 공백으로 이루어진 단어를 count    i.isspace() -> True
            answer += 1
    return answer
