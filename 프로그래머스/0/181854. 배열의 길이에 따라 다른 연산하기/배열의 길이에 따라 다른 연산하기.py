def solution(arr, n):
    answer = []
    for i, c in enumerate(arr):
        if len(arr) % 2 == 0 and i % 2 == 1:
            answer.append(c + n)
        elif len(arr) % 2 == 1 and i % 2 == 0:
            answer.append(c + n)
        else:
            answer.append(c)
    return answer