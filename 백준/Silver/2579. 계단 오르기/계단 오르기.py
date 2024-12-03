from sys import stdin
input = stdin.readline

num = int(input())

dp = [0] * (num + 1)
point = [0] * (num + 1)

for i in range(1, num + 1):
    point[i] = int(input())

if num == 1:
    print(point[1])
    exit()
elif num == 2:
    print(sum(point[:3]))
    exit()

dp[1] = point[1]
dp[2] = point[1] + point[2]

for i in range(3, num + 1):
    dp[i] = max(dp[i - 2] + point[i], dp[i - 3] + point[i - 1] + point[i])

print(dp[-1])