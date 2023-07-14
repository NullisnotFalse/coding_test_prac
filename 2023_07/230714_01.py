# 문자열 정렬하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120850


# isdigit() 사용
def solution_01(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
    return answer


# try/except 사용
def solution_02(my_string):
    answer = []
    for i in my_string:
        try:
            answer.append(int(i))
        except:
            pass
    answer.sort()
    return answer


# 정규표현식 사용
import re


def solution_02(my_string):
    answer = []
    for i in my_string:
        if re.match(r"^\d$", i):
            answer.append(int(i))
    answer.sort()
    return answer
