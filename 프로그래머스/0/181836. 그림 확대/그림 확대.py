def solution(picture, k):
    empty = [''] * len(picture)
    answer= []
    for i, n in enumerate(picture):
        for j in n:
            temp = ''
            j *= k
            temp += j
            empty[i] += temp
    for i in empty:
        for _ in range(k):
            answer.append(i)
    return answer