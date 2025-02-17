from sys import stdin
input = stdin.readline

n = int(input())

cache = [0] * 1001

cache[1] = 1
cache[2] = 2

for i in range(3, 1001):
  cache[i] = (cache[i - 1] + cache[i - 2]) % 10007

print(cache[n])