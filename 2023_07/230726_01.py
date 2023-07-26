# 2차원으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120842


# 반복문과 슬리이싱을 사용한 방법
def solution_01(num_list, n):
    answer = []
    for i in range(len(num_list) // n):
        answer.append(num_list[i * n : ((i + 1) * n)])
    return answer
