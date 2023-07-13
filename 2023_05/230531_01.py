# 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484


# min을 활용한 방법
def solution_01(lottos, win_nums):
    zero_count = lottos.count(0)
    match_count = 0
    for num in lottos:
        if num in win_nums:
            match_count += 1  # 0포함 일치하는 숫자 갯수
    low_rank = min(7 - match_count, 6)  # 0이 다 틀렸다고 가정했을 때 등수 = 최저등수
    high_rank = min(7 - (match_count + zero_count), 6)  # 0이 다 맞았다고 가정했을 때 = 최고등수
    return [high_rank, low_rank]


# 리스트와 count()를 활용한 방법
def solution_02(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return [rank[cnt_0 + ans], rank[ans]]


# 집합을 활용한 방법
def solution_03(lottos, win_nums):
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    return [
        rank[len(set(lottos) & set(win_nums)) + lottos.count(0)],
        rank[len(set(lottos) & set(win_nums))],
    ]
