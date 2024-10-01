from sys import stdin

num, k = map(int, stdin.readline().strip().split())
stones = sorted(list(map(int, stdin.readline().strip().split())))
count = 0
sum = 0

for i in range(num):
    sum += stones[i] * count
    if count < k:
        count += 1
print(sum)