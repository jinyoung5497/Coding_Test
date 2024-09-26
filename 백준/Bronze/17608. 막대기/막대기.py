from sys import stdin

num = int(stdin.readline())
height = [int(stdin.readline()) for _ in range(num)]
height = height[::-1]
stack = []
max_height = 0
answer = 0
for i in range(len(height)):
    if height[i] > max_height:
        max_height = height[i]
        answer += 1
print(answer)
