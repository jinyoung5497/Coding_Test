from sys import stdin

num = int(stdin.readline())
a = sorted(list(map(int, stdin.readline().split())))
b = list(map(int, stdin.readline().split()))
answer = 0

for i in range(num):
    answer += a[i] * max(b)
    b.remove(max(b))
print(answer)