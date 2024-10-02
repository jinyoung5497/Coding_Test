from sys import stdin

num = int(stdin.readline().strip())

for _ in range(num):
    a, b = map(int, stdin.readline().split())

    while True:
        if a == b:
            print(a * 10)
            break
        elif a > b:
            a //= 2
        elif b > a:
            b //= 2
