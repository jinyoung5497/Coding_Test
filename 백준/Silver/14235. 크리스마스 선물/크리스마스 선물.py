from sys import stdin
import heapq

num = int(input())
numbers = []
new_numbers = []

for _ in range(num):
    n = stdin.readline().strip()
    if ' ' in n:
        numbers.append(list(map(int, n.split())))
    else:
        numbers.append(int(n))


for i in numbers:
    if i == 0 and len(new_numbers) == 0:
        print(-1)
    elif i == 0 and len(new_numbers) > 0:
        print(-heapq.heappop(new_numbers))
    elif i != 0:
        for j in range(i[0]):
            heapq.heappush(new_numbers, -i[j + 1])
