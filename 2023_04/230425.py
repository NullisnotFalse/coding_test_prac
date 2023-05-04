# https://school.programmers.co.kr/learn/courses/30/lessons/120822


def solution_01(my_string):
    answer = my_string[::-1]
    return answer


def solution_02(my_string):
    answer = ""
    str_list = list(my_string)
    for i in range(len(my_string)):
        answer += str_list.pop()
    return answer
