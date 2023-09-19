# 두 수 비교하기
# https://www.acmicpc.net/problem/1330


# 조건문


# 풀이

# A,B = map(int,input().split())
A = 1
B = 2


def solution(A, B):
    if A == B:
        return "=="
    elif A > B:
        return ">"
    elif A < B:
        return "<"


print(solution(A, B))
