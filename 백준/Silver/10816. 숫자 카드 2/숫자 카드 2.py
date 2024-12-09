from sys import stdin
input = stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
goal = list(map(int, input().split()))
answer = []
card_dict = {}

for i in cards:
    if i in card_dict:
        card_dict[i] += 1
    else:
        card_dict[i] = 1

for i in goal:
    if i in card_dict:
        answer.append(card_dict[i])
    else:
        answer.append(0)

print(*answer)
