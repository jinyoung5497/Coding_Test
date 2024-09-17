def solution(arr):
    answer = [0] * len(arr)
    prev = arr
    count = 0
    while answer != prev:
        for i in range(len(prev)):
            answer[i] = prev[i]
        for i, n in enumerate(arr):
            if n >= 50 and n % 2 == 0:
                prev[i] = n // 2
            elif n < 50 and n % 2 == 1:
                prev[i] = n * 2 + 1
            else:
                prev[i] = n
        count += 1
    return count - 1