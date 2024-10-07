import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
arr = list(pair())
s = int(input())

for i in range(n):
    if not s:
        break
    max_val = max(arr[i:i+s+1])
    max_idx = arr.index(max_val)
    while max_idx != i and s:
        arr[max_idx], arr[max_idx-1] = arr[max_idx-1], arr[max_idx]
        max_idx -= 1
        s -= 1  

print(*arr)