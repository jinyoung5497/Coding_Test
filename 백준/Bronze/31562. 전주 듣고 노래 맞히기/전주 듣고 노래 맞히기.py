from sys import stdin
n, m = map(int, stdin.readline().split())
music = [stdin.readline().split() for _ in range(n)]
melody = [stdin.readline().split() for _ in range(m)]
melody_dict = {}
count = []
for i in music:
    melody_dict[i[1]] = i[2:5]

for i in melody:
    for j in melody_dict.items():
        if i == j[1]:
            count.append(j[0])
    if len(count) == 0:
        print("!")
    elif len(count) == 1:
        print(count[0])
    elif len(count) >= 2:
        print("?")
    count = []