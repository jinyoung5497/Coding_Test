
from sys import stdin
input = stdin.readline

n = int(input())
ropes = []
for _ in range(n):
    rope = int(input())
    ropes.append(rope)

ropes.sort(reverse=True)
answer = []

for i, n in enumerate(ropes):
    answer.append(n * (i + 1))

print(max(answer))
