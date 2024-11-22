from sys import stdin

num_of_tests = int(stdin.readline())

for _ in range(num_of_tests):
    n, m = map(int, stdin.readline().split())
    empty = [list(map(int, stdin.readline().split())) for i in range(m)]
    print(n - 1)