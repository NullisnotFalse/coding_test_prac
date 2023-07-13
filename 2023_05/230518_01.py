# 주차 요금 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341


import math


def solution(fees, records):
    answer = []

    temp_dict = {}
    time_dict = {}
    for record in records:
        time, number, status = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute)

        if status == "IN":
            temp_dict[number] = minutes
        elif status == "OUT":
            time = minutes - temp_dict[number]
            if number in time_dict:
                time_dict[number] += time
            else:
                time_dict[number] = time
            del temp_dict[number]

    for number, val in temp_dict.items():
        time = 1439 - val
        if number in time_dict:
            time_dict[number] += time
        else:
            time_dict[number] = time

    for number, time in time_dict.items():
        over_time = max(0, time - fees[0])
        total_fees = fees[1] + math.ceil(over_time / fees[2]) * fees[3]
        time_dict[number] = total_fees
    time_dict = sorted(time_dict.items())

    for number, fee in time_dict:
        answer.append(fee)

    return answer
