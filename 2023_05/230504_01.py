# https://school.programmers.co.kr/learn/courses/30/lessons/67256


def solution(numbers, hand):
    temp_dict = {
        1: [[0, 0], "L"],
        2: [[0, 1], "C"],
        3: [[0, 2], "R"],
        4: [[1, 0], "L"],
        5: [[1, 1], "C"],
        6: [[1, 2], "R"],
        7: [[2, 0], "L"],
        8: [[2, 1], "C"],
        9: [[2, 2], "R"],
        0: [[3, 1], "C"],
    }
    numbers_yx = []
    for i in numbers:
        numbers_yx.append(temp_dict[i])
    current_right = [3, 2]
    current_left = [3, 0]
    answer = ""
    for i in numbers_yx:
        if i[1] == "L":
            answer += "L"
            current_left = i[0]
        elif i[1] == "R":
            answer += "R"
            current_right = i[0]
        else:
            left_dis = 0
            right_dis = 0
            left_dis += abs(current_left[0] - i[0][0]) + abs(current_left[1] - i[0][1])
            right_dis += abs(current_right[0] - i[0][0]) + abs(current_right[1] - i[0][1])
            if left_dis < right_dis:
                answer += "L"
                current_left = i[0]
            elif left_dis > right_dis:
                answer += "R"
                current_right = i[0]
            else:
                if hand == "right":
                    answer += "R"
                    current_right = i[0]
                else:
                    answer += "L"
                    current_left = i[0]
    return answer
