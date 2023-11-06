# 대문자와 소문자
# https://school.programmers.co.kr/learn/courses/30/lessons/120893


# 풀이_01 -> .swapcase() 사용


def solution_01(my_string):
    answer = my_string.swapcase()
    return answer



# 풀이_02 -> 반복문, 조건문과 .isupper(), .islower(), .lower(), .upper() 사용


def solution(my_string):
    answer = ''
    for letter in my_string:
        if letter.isupper():
            answer += letter.lower()
        elif letter.islower():
            answer += letter.upper()
    return answer

