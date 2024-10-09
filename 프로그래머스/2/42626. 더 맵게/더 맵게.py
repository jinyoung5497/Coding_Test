import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    min_num = min(scoville)
    if len(scoville) == 1 and scoville[0] > K:
        return 0
    while scoville[0] < K and len(scoville) > 1:
        a1 = heapq.heappop(scoville)
        b1 = heapq.heappop(scoville)
        temp = a1 + (b1 * 2)
        answer += 1
        heapq.heappush(scoville, temp)

    if scoville[0] >= K:
        return answer
    else:
        return -1