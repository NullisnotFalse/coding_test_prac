# 인덱스 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/120895


# 풀이_01 -> list를 사용한 방법


def solution(my_string, num1, num2):
    str_list = list(map(str,my_string))
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]
    answer = ''.join(str_list)
    return answer