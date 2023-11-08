# 숫자 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120904


# 풀이_01 -> .index() 사용


def solution_01(num, k):
    answer = -1
    num_list = list(map(int,str(num)))
    try:
        answer = num_list.index(k) + 1
    except:
        pass
    return answer


# 풀이_02 -> 반복문, enumerate() 사용


def solution_02(num, k):
    answer = -1
    num_list = list(map(int,str(num)))
    for i,value in enumerate(num_list):
        if value == k:
            answer = i + 1
            break
    return answer