num = int(input())
word = input()
answer = 0

for i in range(len(word)):
    value = ord(word[i]) - 96
    answer += value * (31 ** i)

print(answer)