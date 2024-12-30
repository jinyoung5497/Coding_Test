from sys import stdin

input = stdin.readline

num = list(input().strip().split('-'))

numbers = []
for i in num:
    numbers.append(list(map(int, i.split('+'))))

answer = []
for i in numbers:
    answer.append(sum(i))

total = answer[0]
for i in range(1, len(answer)):
    if i == 0:
        continue
    total -= answer[i]

print(total)