# https://school.programmers.co.kr/learn/courses/30/lessons/172928 - 공원 산책


def solution(park, routes):
    current = []
    hurdles = []

    # 시작지점 좌표 찾아서 저장
    for i in range(len(park)):
        if "S" in park[i]:
            current = [i, park[i].find("S")]

    # 장애물 좌표 찾아서 저장
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "X":
                hurdles.append([i, j])

    for vector in routes:
        if vector[0] == "E":
            for i in range(1, int(vector[2]) + 1):
                next = [current[0], current[1] + i]
                if next in hurdles or not (0 <= next[1] < len(park[0])):
                    break
            else:
                current = next

        elif vector[0] == "W":
            for i in range(1, int(vector[2]) + 1):
                next = [current[0], current[1] - i]
                if next in hurdles or not (0 <= next[1] < len(park[0])):
                    break
            else:
                current = next

        elif vector[0] == "S":
            for i in range(1, int(vector[2]) + 1):
                next = [current[0] + i, current[1]]
                if next in hurdles or not (0 <= next[0] < len(park)):
                    break
            else:
                current = next

        elif vector[0] == "N":
            for i in range(1, int(vector[2]) + 1):
                next = [current[0] - i, current[1]]
                if next in hurdles or not (0 <= next[0] < len(park)):
                    break
            else:
                current = next

    return current
