from sys import stdin

input = stdin.readline

n = int(input())
switch = list(map(int, input().split()))
m = int(input())
option = []
for _ in range(m):
    a, b = map(int, input().split())
    option.append([a, b])

for a, b in option:
    if a == 1:
        idx = len(switch) // b
        for i in range(1, idx+1):
            new_idx = b * i - 1
            if switch[new_idx] == 0:
                switch[new_idx] = 1
            else:
                switch[new_idx] = 0
    else:
        curr = b - 1
        idx = 0
        while 0 <= curr-idx and curr+idx < len(switch) and switch[curr-idx] == switch[curr+idx]:
            pos = curr+idx
            neg = curr-idx
            if pos == neg:
                if switch[pos] == 0:
                    switch[pos] = 1
                else:
                    switch[pos] = 0
                idx += 1
                continue
            if switch[pos] == 0:
                switch[pos] = 1
            else:
                switch[pos] = 0
            if switch[neg] == 0:
                switch[neg] = 1
            else:
                switch[neg] = 0

            idx += 1

for i in range(len(switch)):
    if (i+1) % 20 == 0:
        print(switch[i])
    else:
        print(switch[i], end=' ')