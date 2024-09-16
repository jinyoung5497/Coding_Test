def solution(num_list):
    answer = 0
    temp = 0
    for i in num_list:
        temp = i
        while temp > 1:
            if temp % 2 == 0:
                temp /= 2
            else:
                temp = (temp - 1) / 2
            if temp >= 1:
                answer += 1
        
    return answer