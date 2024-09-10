n = int(input())

# 위쪽 피라미드 출력
for i in range(1, n + 1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)

# 아래쪽 피라미드 출력
for i in range(n - 1, 0, -1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)