# 시험 성적
# https://www.acmicpc.net/problem/9498


# 조건문


# 풀이 1

# N = int(input())
N = 100


def solution(N):
    if 100 >= N >= 90:
        return "A"
    elif 89 >= N >= 80:
        return "B"
    elif 79 >= N >= 70:
        return "C"
    elif 69 >= N >= 60:
        return "D"
    else:
        return "F"


print(solution(N))


# 풀이 2

# M = int(input())
M = 100


def solution(M):
    if M >= 90:
        return "A"
    elif M >= 80:
        return "B"
    elif M >= 70:
        return "C"
    elif M >= 60:
        return "D"
    else:
        return "F"


print(solution(M))


# elif가 나열되어 있는 경우에는 위에서부터 차례대로 조건을 제외하면서 실행되므로 불필요한 범위 값을 지정할 필요가 없음
# 풀이 1은 실행시간 44m / 풀이 2는 실행시간 40m
