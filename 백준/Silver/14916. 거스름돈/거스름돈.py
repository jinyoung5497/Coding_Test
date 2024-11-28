from sys import stdin
input = stdin.readline

coins = [5, 2]

n = int(input())
count = 0
rest = n % 5
for i in coins:
    if n >= i:
        if i == 5 and rest % 2 != 0:
            value = n // i
            count = value - 1
            n -= i * count
        else:
            count += n // i
            n %= i

if n % 2 == 0:
    print(count)
else:
    print(-1)