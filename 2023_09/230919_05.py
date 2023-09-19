# 알람 시계
# https://www.acmicpc.net/problem/2884


# 조건문


# 풀이_1

# H_1,M_1 = map(int,input().split())
H_1 = 10
M_1 = 10


def solution_1(H_1, M_1):
    if M_1 < 45:
        if H_1 != 0:
            return H_1 - 1, 60 + (M_1 - 45)
        elif H_1 == 0:
            return 23, 60 + (M_1 - 45)
    elif M_1 >= 45:
        return H_1, M_1 - 45


print(*solution_1(H_1, M_1))


# 풀이_1 실행 시간 40m
