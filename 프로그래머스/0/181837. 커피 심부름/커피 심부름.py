def solution(order):
    answer = 0
    hot = ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]
    for i in order:
        if i in hot:
            answer += 5000
        else:
            answer += 4500
    return answer