# 블랙잭
# https://www.acmicpc.net/problem/2798


# 알고리즘 분류 : Brute Force (완전 탐색)


# 생각해야 할 것
"""
1. 조합 사용 -> 조합 리스트의 각 원소가 튜플 형태로 반환
2. 각각 튜플의 합을 원소로 하는 리스트 생성
3. M값을 넘지 않는 최대값을 구함
"""


from itertools import combinations


# N,M = map(int,input().split())
# card_list = list(map(int, input().split()))

N = 5
M = 21
card_list = [5, 6, 7, 8, 9]


# 튜플로 이루어진 리스트를 가지고 각 튜플 원소들의 합으로 이루어진 리스트를 return하는 함수
def sum_selected_cards(selected_card_list):
    sum_cards_list = []
    for selected_cards in selected_card_list:
        sum_result = sum(selected_cards)
        sum_cards_list.append(sum_result)
    return sum_cards_list


# M보다 작은 최대값을 return하는 함수
def max_check(sum_cards_list, M):
    max_check_list = []
    for element in sum_cards_list:
        if element <= M:
            max_check_list.append(element)
    max_value = max(max_check_list)
    return max_value


# 실행 함수
def solution(N, M, card_list):
    selected_card_list = list(combinations(card_list, 3))
    sum_cards_list = sum_selected_cards(selected_card_list)
    answer = max_check(sum_cards_list, M)
    return answer


print(solution(N, M, card_list))
