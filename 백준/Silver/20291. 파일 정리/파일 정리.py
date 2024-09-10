input_num = int(input())
file_list = [input().split('.')[-1] for _ in range(input_num)]
file = {}

for item in file_list:
    if item in file:
        file[item] += 1
    else:
        file[item] = 1

for file, count in sorted(file.items()):
    print(f"{file} {count}")