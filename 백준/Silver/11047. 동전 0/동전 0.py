from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coins = []
for i in range(n):
    coin = int(input())
    coins.append(coin)

reversed_coins = sorted(coins, reverse=True)
count = 0
for i in reversed_coins:
    if k == 0:
        break
    if i <= k:
        count += k // i
        k %= i

print(count)