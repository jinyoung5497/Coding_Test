def solution(arr, queries):
    answer = []
    for a, b, c in queries:
        for i in range(a, b + 1):
            if i % c == 0:
                arr[i] = arr[i] + 1
                
    return arr