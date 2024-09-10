def solution(a, b):
    res1 = int(str(a) + str(b))
    res2 = int(str(b) + str(a))
    if res1 > res2:
        return res1
    else: return res2