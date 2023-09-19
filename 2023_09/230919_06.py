# 오븐 시계
# https://www.acmicpc.net/problem/2525


# 조건문


# 생각해야 할 것
"""
1. 요리 시간을 분 단위에서 시간, 분 단위로 변환
2. 현재 시각에서 분과 요리 시간에서 분이 60 이상일 경우 시간에 1을 더해주고 나머지 분을 0에서 더해줘야 함
3. 그 후에 현재 시각에서 시간과 요리 시간에서 시간이 24 이상일 경우 나머지 시간을 0에서 더해줘야 함
"""


# 풀이_1

# A_1,B_1 = map(int,input().split())
# C_1 = int(input())
A_1 = 14
B_1 = 30
C_1 = 20


# 요리 시간을 시간, 분 단위로 변환하는 함수
def cook_time(C_1):
    cook_h = C_1 // 60
    cook_m = C_1 % 60
    return cook_h, cook_m


# 실행 함수
def solution_1(A_1, B_1, C_1):
    h = 0
    m = 0
    temp_h = 0
    cook_h, cook_m = cook_time(C_1)
    if B_1 + cook_m >= 60:
        temp_h += 1
        m = (B_1 + cook_m) - 60
    elif B_1 + cook_m < 60:
        m = B_1 + cook_m
    if A_1 + temp_h + cook_h >= 24:
        h = (A_1 + temp_h + cook_h) - 24
    elif A_1 + temp_h + cook_h < 24:
        h = A_1 + temp_h + cook_h
    return h, m


print(*solution_1(A_1, B_1, C_1))


# 풀이_1 실행 시간 40m
