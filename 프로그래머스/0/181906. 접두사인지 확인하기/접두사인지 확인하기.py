def solution(my_string, is_prefix):
    answer = 0
    for i in range(len(is_prefix)):
        if len(is_prefix) < len(my_string):
            if my_string[i] != is_prefix[i]:
                answer = 0
                break
            else:
                answer = 1
    return answer