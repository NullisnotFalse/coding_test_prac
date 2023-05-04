# https://school.programmers.co.kr/learn/courses/30/lessons/178871


def solution(players, callings):
    dict = {name: rank for rank, name in enumerate(players)}
    for call in callings:
        i = dict[call]
        players[i - 1], players[i] = players[i], players[i - 1]
        dict[call] -= 1
        dict[players[i]] += 1
    return players
