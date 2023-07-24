# 중복된 문자 제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120888


# 반복문과 조건문을 사용하는 방법
def solution_01(my_string):
    answer = ""
    for i in my_string:
        if i not in answer:
            answer += i
    return answer


# 집합을 이용하는 방법 - 순서가 무작위로 바뀌어서 실패
def solution_02_fail(my_string):
    temp_set = set(my_string)
    answer = "".join(temp_set)
    return answer


# collections 모듈의 OrderedDict 클래스를 사용하는 방법
from collections import OrderedDict


def solution(my_string):
    temp_dict = OrderedDict.fromkeys(my_string)
    answer = "".join(temp_dict)
    return answer
