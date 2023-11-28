# 문자열 내 마음대로 정렬하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12915


# 풀이_01 -> 딕셔너리와 정렬 활용


def solution(strings, n):
    strings.sort()
    temp_dict = {}
    for string in strings:
        temp_dict[string] = string[n]
    sorted_dict = dict(sorted(temp_dict.items(), key=lambda item: item[1]))
    answer = list(sorted_dict.keys())
    return answer


"""
실행결과
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉 통과 (0.03ms, 10.1MB)
테스트 11 〉 통과 (0.01ms, 10.3MB)
테스트 12 〉 통과 (0.03ms, 10.1MB)
"""
