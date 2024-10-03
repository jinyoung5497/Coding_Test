from sys import stdin

num = int(stdin.readline())
for _ in range(num):
    _ = stdin.readline().strip()
    s, b = map(int, stdin.readline().split())
    sejun = sorted(list(map(int, stdin.readline().split())), reverse=True)
    sebie = sorted(list(map(int, stdin.readline().split())), reverse=True)

    for i in range(s + b):
        if not sebie or not sejun:
            break
        if sejun[-1] >= sebie[-1]:
            sebie.pop()
        else:
            sejun.pop()
    if sejun:
        print('S')
    elif sebie:
        print('B')
    else:
        print('C')