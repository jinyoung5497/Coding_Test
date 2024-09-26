from sys import stdin

num = stdin.readline().strip()
count = 0
while len(num) > 1:
    answer = 0
    for i in str(num):
        answer += int(i)
    count += 1
    num = str(answer)

print(count)
if int(num) % 3 == 0:
    print("YES")
else:
    print("NO")