def solution(arr, k):
    answer = []
    for i in arr:
        if i in answer:
            continue
        else:
            answer.append(i)
    if k > len(answer):
        for _ in range(k - len(answer)):
            answer.append(-1)
    else: 
        answer = answer[:k]
    return answer