n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

result = []

for i in range(n):
   grid[i] = grid[i][::-1]

result = [''.join(i) for i in grid]

for i in result:
    print(i)