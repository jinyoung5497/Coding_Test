def solution(rank, attendance):
    answer = []
    for i, b in enumerate(attendance):
        if b:
            answer.append((rank[i], i))
    answer = sorted(answer, key= lambda x: x[0])
    a,b,c = answer[0][1], answer[1][1], answer[2][1]
    
    return 10000 * a + 100 * b + c