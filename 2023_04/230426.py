# https://school.programmers.co.kr/learn/courses/30/lessons/17686


import re


def slice_f(file):
    file = file.lower()
    head = re.findall("\D+", file)[0]
    number = int(re.findall("\d+", file)[0])
    tail = file[len(re.findall("\D+", file)[0]) + len(re.findall("\d+", file)[0]) :]
    slice_file = [head, number, tail]
    return slice_file


def solution(files):
    files_dict = {}
    for index, file in enumerate(files):
        files_dict[index] = slice_f(file)
    sorted_files = sorted(files_dict.items(), key=lambda x: (x[1][0], x[1][1]))
    answer = []
    for i in sorted_files:
        answer.append(files[i[0]])
    return answer
