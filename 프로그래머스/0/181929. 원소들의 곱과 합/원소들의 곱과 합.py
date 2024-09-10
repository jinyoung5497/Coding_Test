def solution(num_list):
    answer = 0
    res1 = 1
    res2 = 0
    for i in num_list:
        res1 *= i
        res2 += i
    if res1 < res2 ** 2:
        answer = 1
    else: answer = 0
    return answer