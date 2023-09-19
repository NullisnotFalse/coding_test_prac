# 분해합
# https://www.acmicpc.net/problem/2231


# 알고리즘 분류 : Brute Force (완전 탐색)


# 생각해야 할 것
"""
1. 가능한 모든 생성자를 완전 탐색으로 뽑아서 리스트 생성
    1-1) 가능한 생성자의 최솟값은 N/2
2. 리스트에서 가장 작은 값을 반환
    2-1) 리스트가 비어있을 경우 0을 반환
"""


# 풀이_1

# N = int(input())
N = 216


# 분해합을 만드는 함수
def create_generator(num):
    str_list = list(str(num))
    int_list = []
    for element in str_list:
        int_list.append(int(element))
    result = num + sum(int_list)
    return result


# 생성자 리스트를 만드는 함수
def create_generator_list(N):
    generator_list = []
    for num in range(int(N / 2), N):
        if create_generator(num) == N:
            generator_list.append(num)
    return generator_list


# 실행 함수
def solution_1(N):
    generator_list = create_generator_list(N)
    try:
        return min(generator_list)
    except:
        return 0


print(solution_1(N))


# 풀이 후 생각해 본 것
"""
1. create_generator_list(N) 함수에서 range(int(N / 2), N)는 가장 작은 값부터 1씩 커지면서 반복함
    1-1) 따라서 처음 발견된 생성자가 가장 작은 값이므로 생성자가 발견되면 그대로 break를 해도 됨
"""


# 풀이_2


# create_generator() 함수는 재사용


# 가장 작은 생성자를 찾는 함수
def create_min_generator(N):
    min_generator = 0
    for num in range(int(N / 2), N):
        if create_generator(num) == N:
            min_generator = num
            break
    return min_generator


# 실행 함수
def solution_2(N):
    min_generator = create_min_generator(N)
    return min_generator


print(solution_2(N))
