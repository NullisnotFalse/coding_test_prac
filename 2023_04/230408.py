# https://school.programmers.co.kr/learn/courses/30/lessons/120875


def solution(dots):
    for i in dots:
        dot_list = dots.copy()
        dot_list.remove(i)
        for j in dot_list:
            dot_list2 = dot_list.copy()
            dot_list2.remove(j)
            dot_x = (i[1] - j[1]) / (i[0] - j[0])
            dot_y = (dot_list2[0][1] - dot_list2[1][1]) / (
                dot_list2[0][0] - dot_list2[1][0]
            )
            if dot_x == dot_y:
                return 1
    return 0
