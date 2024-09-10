def solution(a, b):
    res1 = str(a) + str(b)
    res2 = 2 * a * b
    answer = max(int(res1), res2)
    return answer