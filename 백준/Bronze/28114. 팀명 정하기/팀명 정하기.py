from sys import stdin

num = 3
name = [list(map(str, stdin.readline().split())) for _ in range(num)]
first_name = []
second_name = []
temp = ''
for i in name:
    a, b, c = i
    new_b = int(b) % 100
    first_name.append(new_b)
    second_name.append((a, c))

new_second_name = sorted(second_name, key=lambda x: int(x[0]), reverse=True)
print(''.join(map(str, sorted(first_name))))
for _, i in new_second_name:
    temp = temp + i[0]
print(temp)