# https://school.programmers.co.kr/learn/courses/30/lessons/120894


def solution_01(numbers):
    answer = ""
    while numbers != "":
        if numbers[:3] == "one":
            answer += "1"
            numbers = numbers[3:]
        elif numbers[:3] == "two":
            answer += "2"
            numbers = numbers[3:]
        elif numbers[:3] == "thr":
            answer += "3"
            numbers = numbers[5:]
        elif numbers[:3] == "fou":
            answer += "4"
            numbers = numbers[4:]
        elif numbers[:3] == "fiv":
            answer += "5"
            numbers = numbers[4:]
        elif numbers[:3] == "six":
            answer += "6"
            numbers = numbers[3:]
        elif numbers[:3] == "sev":
            answer += "7"
            numbers = numbers[5:]
        elif numbers[:3] == "eig":
            answer += "8"
            numbers = numbers[5:]
        elif numbers[:3] == "nin":
            answer += "9"
            numbers = numbers[4:]
        elif numbers[:3] == "zer":
            answer += "0"
            numbers = numbers[4:]
    answer = int(answer)
    return answer


def solution_02(numbers):
    answer = ""
    temp_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }


# 나중에 완성


# replace 쓰는 방법도 써보기
