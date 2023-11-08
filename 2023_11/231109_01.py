# 배열의 유사도
# https://school.programmers.co.kr/learn/courses/30/lessons/120903


# 풀이_01 -> 반복문, 조건문을 사용한 방법


def solution_01(s1,s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer


# 풀이_02 -> 교집합을 사용한 방법


def solution_02(s1,s2):
    answer = len(set(s1)&set(s2))
    return answer