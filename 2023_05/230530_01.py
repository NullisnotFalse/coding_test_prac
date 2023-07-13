# 신규 아이디 추천
# https://school.programmers.co.kr/learn/courses/30/lessons/72410


import re


def solution(new_id):
    new_id = new_id.lower()

    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    # re.sub(정규표현식, 치환 문자, 대상 문자열） -> 대상 문자열에서 정규표현식에 맞는 문자를 치환 문자로 치환한다.

    # p = re.compile("[^a-z0-9-_.]")
    # new_id_list = p.findall(new_id)

    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)

    # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub(r"\.{2,}", ".", new_id)

    # 마침표(.)가 처음이나 끝에 위치한다면 제거
    # new_id = re.sub(r"^\.", "", new_id)  # 처음
    # new_id = re.sub(r"\.$", "", new_id)  # 끝
    new_id = re.sub("^[.]|[.]$", "", new_id)

    # 빈 문자열이라면, new_id에 "a"를 대입
    if new_id == "":
        new_id = "a"

    # 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거 / 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub(r"\.$", "", new_id)  # 끝

    # 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id
