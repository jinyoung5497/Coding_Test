from sys import stdin

n, m = map(int, stdin.readline().split())
cord = list(map(int, stdin.readline().split()))
cord.sort()
start, end = 0, n - 1

def binary_min(a, start, end):
    while start <= end:
        mid = (start + end) // 2
        if cord[mid] >= a:
            end = mid - 1
        else:
            start = mid + 1
    return end + 1
def binary_max(b, start, end):
    while start <= end:
        mid = (start + end) // 2
        if cord[mid] <= b:
            start = mid + 1
        else:
            end = mid - 1
    return end

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    min_index = binary_min(a, start, end)
    max_index = binary_max(b, start, end)
    count = 0
    for i in range(min_index, max_index + 1):
        count += 1
    print(count)