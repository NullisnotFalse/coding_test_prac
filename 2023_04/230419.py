# https://school.programmers.co.kr/learn/courses/30/lessons/92334


def solution(id_list, report, k):
    count_dict = {}
    mailed_dict = {}
    reporter_dict = {}
    target_dict = {}

    for i in id_list:
        count_dict[i] = 0
        mailed_dict[i] = 0

    report = set(report)
    for key, value in enumerate(report):
        reporter = value.split(" ")[0]
        reporter_dict[key] = reporter
        target = value.split(" ")[1]
        target_dict[key] = target

    for i in target_dict:
        target = target_dict[i]
        count_dict[target] += 1

    for name in count_dict:
        if count_dict[name] >= k:
            for index in target_dict:
                if target_dict[index] == name:
                    mailed = reporter_dict[index]
                    mailed_dict[mailed] += 1
    answer = list(mailed_dict.values())
    return answer
