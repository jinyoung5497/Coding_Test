from sys import stdin

num = int(stdin.readline())
for _ in range(num):
    temp = []
    case = int(stdin.readline())
    for _ in range(case):
        uni = stdin.readline().split()
        temp.append(uni)
    sorted_list = sorted(temp, key=lambda x: int(x[1]), reverse=True)
    print(sorted_list[0][0])