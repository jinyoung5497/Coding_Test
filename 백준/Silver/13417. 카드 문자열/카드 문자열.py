from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    words = list(input().split())
    q = deque()
    q.append(words[0])
    for i in range(1, len(words)):
        first = q.popleft()
        second = words[i]
        word_a = first + second
        word_b = second + first
        if word_a < word_b:
            q.append(word_a)
        else:
            q.append(word_b)

    print(*q)