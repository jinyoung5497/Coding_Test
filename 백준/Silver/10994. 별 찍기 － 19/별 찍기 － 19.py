# 입력값
input_num = int(input())
# size에 해당하는 빈배열 만들기
star_list = [[' ' for _ in range(input_num + (3 * (input_num - 1)))] for _ in range(input_num + (3 * (input_num - 1)))]


def asterisk(n, x, y):
    if n == 1:
        star_list[x][y] = '*'
        return
    size = n + (3 * (n - 1))
    for i in range(size):
        star_list[y][x + i] = '*'
        star_list[y + i][x] = '*'
        star_list[y + size - 1][x + i] = '*'
        star_list[y + i][x + size - 1] = '*'

    asterisk(n - 1, x + 2, y + 2)


asterisk(input_num, 0, 0)
for star in star_list:
    print(''.join(star))