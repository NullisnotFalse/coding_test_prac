# https://school.programmers.co.kr/learn/courses/30/lessons/118666


def solution(survey, choices):
    point_dict = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    temp_dict = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    for index, choice in enumerate(choices):
        if choice < 4:
            point_dict[survey[index][0]] += temp_dict[choice]
        elif choice > 4:
            point_dict[survey[index][1]] += temp_dict[choice]
    if point_dict["R"] >= point_dict["T"]:
        del point_dict["T"]
    else:
        del point_dict["R"]
    if point_dict["C"] >= point_dict["F"]:
        del point_dict["F"]
    else:
        del point_dict["C"]
    if point_dict["J"] >= point_dict["M"]:
        del point_dict["M"]
    else:
        del point_dict["J"]
    if point_dict["A"] >= point_dict["N"]:
        del point_dict["N"]
    else:
        del point_dict["A"]
    answer = "".join(point_dict.keys())
    return answer
