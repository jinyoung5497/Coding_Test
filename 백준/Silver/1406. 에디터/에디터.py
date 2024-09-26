from sys import stdin
input = stdin.readline().strip()
left = [i for i in input]
right = []
num = int(stdin.readline().strip())

for _ in range(num):
    cmd = stdin.readline().strip().split()
    if cmd[0] == "L" and left:
        right.append(left.pop())
    elif cmd[0] == "D" and right:
        left += right.pop()
    elif cmd[0] == "B" and left:
        left.pop()
    elif cmd[0] == "P":
        left += cmd[1]
print("".join(left + right[::-1]))