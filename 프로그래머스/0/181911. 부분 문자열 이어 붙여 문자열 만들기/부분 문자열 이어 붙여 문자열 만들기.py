def solution(my_strings, parts):
    answer = ''
    for a, b in enumerate(parts):
        answer += my_strings[a][b[0]:b[1] + 1]
    return answer