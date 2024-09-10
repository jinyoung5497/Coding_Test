def solution(num_list):
    answer = 0
    for i, c in enumerate(num_list):
        if c < 0:
            answer = i
            break
        else:
            answer = -1
    return answer