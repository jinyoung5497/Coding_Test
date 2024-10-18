def solution(clothes):
    answer = {}
    count = 0
    calc = 1
    for i in clothes:
        if i[1] in answer.keys():
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1
    for i in answer.values():
        calc *= i + 1

    count =  calc - 1


    return count