# 연속된 수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/120923


# 풀이_01 -> 반복문, 연산자 사용


def solution(num, total):
    n = (total // num) + (num // 2)
    answer = []
    for i in range(num):
        answer.append(n - i)
    answer.sort()
    return answer
