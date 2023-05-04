# https://school.programmers.co.kr/learn/courses/30/lessons/176963


# 지연시간 길었음 (10.46ms)
def solution_01(name, yearning, photo):
    score_dict = {}
    for i in range(len(name)):
        score_dict[name[i]] = yearning[i]
    answer = []
    for i in photo:
        score = 0
        for sum in name:
            if sum in i:
                score += score_dict[sum]
        answer.append(score)
    return answer


# 지연시간 짧았음 (1.04ms)
def solution_02(name, yearning, photo):
    answer = []
    score_dict = {}
    for i, j in zip(name, yearning):
        score_dict[i] = j
    for i in photo:
        score = 0
        for j in i:
            if j in score_dict:
                score += score_dict[j]
        answer.append(score)
    return answer
