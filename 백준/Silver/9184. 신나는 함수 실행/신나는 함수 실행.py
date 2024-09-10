input_list = []
ans_list = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while True:
    input_num = list(map(int, input().split()))

    if input_num == [-1, -1, -1]:
            break
    input_list.append(input_num)


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if ans_list[a][b][c]:
        return ans_list[a][b][c]
    if a < b < c:
        ans_list[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return ans_list[a][b][c]
    else:
        ans_list[a][b][c] = (w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1))
        return ans_list[a][b][c]


for i in input_list:
    print(f"w({i[0]}, {i[1]}, {i[2]}) =", w(i[0], i[1], i[2]))
