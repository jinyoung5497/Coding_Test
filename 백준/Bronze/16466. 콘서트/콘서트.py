from sys import stdin

num = int(stdin.readline())
ticket = sorted(list(map(int, stdin.readline().split())))
min_ticket = 1
for i in range(num):
    if ticket[i] == min_ticket:
        min_ticket += 1
print(min_ticket)