# 겹치는 선분의 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/120876


"""
제한사항
1) lines의 길이 = 3
2) lines의 원소의 길이 = 2
3) 모든 선분은 길이가 1 이상입니다.
4) lines의 원소는 [a, b] 형태이며, a, b는 각각 선분의 양 끝점 입니다.
    -> -100 ≤ a < b ≤ 100
"""

"""
생각해야 할 것
1) 3개의 선분이 전부 다 겹칠수도 있음
    -> 2개가 겹치는 거랑 3개가 겹치는 거랑 겹치는 길이는 똑같이 처리되어야 함
2) 3개의 선분 사이에 비어있는 공간이 있을수도 있음 (아예 안겹치고 떨어져 있는 경우)
"""

# 1차 풀이
"""
풀이과정
1) 선분을 시작점과 끝점의 좌표 형태에서 수직선의 각각의 정수에 매치되는 리스트 형태로 변경
    -> 반복문 사용 / 시간복잡도는 3N
2) 선분A와 B, 선분B와 C, 선분A와 C를 각각 비교해서 겹치는 원소가 있을 경우 새로운 리스트에 추가
    -> 반복문 사용 / 시간복잡도는 3N
3) 겹치는 원소들을 모아놓은 리스트에서 길이를 구함
    -> 주의할 점은 3개 선분이 다 겹칠 경우를 생각해서 3개가 겹치는 경우를 빼줘야 함
    -> 겹치는 원소가 없을 경우에는 TypeError가 나기 때문에 try / except문으로 빈 리스트 일때 길이를 0으로 반환해줘야함
"""


def line_convert(line):
    line_list = []
    for i in range(line[0], line[1] + 1, 1):
        line_list.append(i)
    return line_list


def overlap_check(list1, list2):
    overlap_list = []
    for i in list1:
        if i in list2:
            overlap_list.append(i)
    return overlap_list


def answer_calc(list):
    try:
        return list[-1] - list[0]
    except:
        return 0


def solution(lines):
    line1_list = line_convert(lines[0])
    line2_list = line_convert(lines[1])
    line3_list = line_convert(lines[2])
    overlap_list1 = overlap_check(line1_list, line2_list)
    overlap_list2 = overlap_check(line2_list, line3_list)
    overlap_list3 = overlap_check(line1_list, line3_list)
    triple_overlap_list1 = overlap_check(overlap_list1, overlap_list2)
    triple_overlap_list2 = overlap_check(overlap_list2, overlap_list3)

    answer = (
        answer_calc(overlap_list1)
        + answer_calc(overlap_list2)
        + answer_calc(overlap_list3)
        - answer_calc(triple_overlap_list1)
        - answer_calc(triple_overlap_list2)
    )

    return answer
