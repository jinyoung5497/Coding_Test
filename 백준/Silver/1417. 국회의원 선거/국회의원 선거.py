import heapq

num = int(input())
count = 0
heap = []
my_votes = 0
for i in range(num):
    votes = int(input())
    if i == 0:
        my_votes = votes
        continue
    heapq.heappush(heap, -votes)

while heap:
    votes = -heapq.heappop(heap)
    if my_votes > votes:
        break
    my_votes += 1
    count += 1
    heapq.heappush(heap, -(votes - 1))

print(count)

