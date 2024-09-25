from sys import stdin
input = int(stdin.readline())
strInput = [stdin.readline().strip() for _ in range(input)]
stack = []
answer = 0

for i in strInput:
    for j, c in enumerate(i):
        stack.append(c)
        if len(stack) > 1 and c == stack[-2]:
            stack.pop()
            stack.pop()
    if len(stack) == 0:
        answer += 1
    stack = []
print(answer)