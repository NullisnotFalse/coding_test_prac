# 로그인 성공?
# https://school.programmers.co.kr/learn/courses/30/lessons/120883


# 풀이_01 -> 반복문, 조건문 사용


def solution(id_pw, db):
    for db_data in db:
        if id_pw[0] == db_data[0]:
            if id_pw[1] == db_data[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"
