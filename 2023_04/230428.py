# https://school.programmers.co.kr/learn/courses/30/lessons/17681


def list_check(n, arr1_list, arr2_list):
    arr_list = []
    for y in range(n):
        temp = ""
        for x in range(n):
            if arr1_list[y][x] == "0" and arr2_list[y][x] == "0":
                temp += " "
            else:
                temp += "#"
        arr_list.append(temp)
    return arr_list


def solution(n, arr1, arr2):
    arr1_list = []
    arr2_list = []
    for i in range(n):
        arr1_list += [format(arr1[i], f"0{n}b")]
        arr2_list += [format(arr2[i], f"0{n}b")]
    answer = list_check(n, arr1_list, arr2_list)
    return answer
