from sys import stdin
from itertools import product

input = stdin.readline

n = int(input())
test = [int(input()) for _ in range(n)]

big_num = max(test)
dp = [0] * (big_num+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, big_num+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in test:
    print(dp[i])