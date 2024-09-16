def solution(arr):
    answer = [0] * 2 
    while len(arr) > len(answer):
        answer *= 2
    for i in range(len(arr)):
        answer[i] = arr[i] 
    if len(arr) == 1:
        answer = arr
    return answer