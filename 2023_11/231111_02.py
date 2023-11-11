# 이진수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120885


# 풀이_01 -> int(), bin() 사용


def solution(bin1, bin2):
    answer = str(bin(int(bin1, 2) + int(bin2, 2)))[2:]
    return answer
