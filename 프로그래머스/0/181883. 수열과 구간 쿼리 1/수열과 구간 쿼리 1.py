def solution(arr, queries):
    answer = []
    for a,b in queries:
        for i in range(a, b + 1):
            arr[i] += 1
    return arr