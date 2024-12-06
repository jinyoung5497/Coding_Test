from sys import stdin
input = stdin.readline

n = int(input())
budget = sorted(list(map(int, input().split())))
goal = int(input())
start = 0
end = max(budget)

if sum(budget) < goal:
    print(end)
    exit()

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(len(budget)):
        if budget[i] > mid:
            total += mid
        else:
            total += budget[i]

    if total > goal:
        end = mid - 1
    else:
        start = mid + 1

print(end)