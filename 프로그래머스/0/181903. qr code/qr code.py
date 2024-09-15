def solution(q, r, code):
    answer = ''
    for i, c in enumerate(code):
        if i % q == r:
            answer += c
    return answer