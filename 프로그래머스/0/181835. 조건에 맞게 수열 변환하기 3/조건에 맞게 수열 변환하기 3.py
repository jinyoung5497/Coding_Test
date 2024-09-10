def solution(arr, k):
    answer = []
    for i in arr:
        if k % 2 == 1:
            answer.append(i * k)
        else:
            answer.append(i + k)
    return answer