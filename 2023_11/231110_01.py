# 문자열 정렬하기2
# https://school.programmers.co.kr/learn/courses/30/lessons/120911


# 풀이_01 -> .lower()와 sorted() 사용
# sort()는 리스트에만 사용 가능 / sorted()는 이터러블 객체 전부 사용 가능


def solution(my_string):
    answer = ''.join(sorted(my_string.lower()))
    return answer