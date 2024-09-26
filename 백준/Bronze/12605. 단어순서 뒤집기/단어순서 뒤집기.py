from sys import stdin

num = int(stdin.readline())
input_list = [stdin.readline().split() for _ in range(num)]
new_list = []
for i, n in enumerate(input_list):
    new_list.append(' '.join(n[::-1]))
    print(f"Case #{i + 1}: {new_list[i]}")