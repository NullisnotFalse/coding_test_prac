# 머쓱이보다 키 큰 사람
# https://school.programmers.co.kr/learn/courses/30/lessons/120585


# 풀이_01 -> 반복문, 조건문, .sort() 사용


def solution_01(array, height):
    answer = 0
    array.sort(reverse=True)
    for i in array:
        if i > height:
            answer += 1
        else:
            break
    return answer


# 풀이_02 -> .append() .sort() .index() 사용


def solution_02(array, height):
    array.append(height)
    array.sort(reverse=True)
    answer = array.index(height)
    return answer