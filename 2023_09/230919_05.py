# 알람 시계
# https://www.acmicpc.net/problem/2884


# 조건문


# 풀이_1

# H,M = map(int,input().split())
H = 10
M = 10


def solution_1(H, M):
    if M < 45:
        if H != 0:
            return H - 1, 60 + (M - 45)
        elif H == 0:
            return 23, 60 + (M - 45)
    elif M >= 45:
        return H, M - 45


print(*solution_1(H, M))


# 풀이_1 실행 시간 40m
