def solution(n):
    global answer
    answer = [[0 for _ in range(n)]for _ in range(n)]
    assign(0,0,1,n);
    return answer

def assign(y, x, num, n):
    if(n<=0):return answer
    answer[y][x] = num
    for _ in range(1, n):#→
        x+=1
        num+=1
        answer[y][x]=num
    for _ in range(1, n):#↓
        y+=1
        num+=1
        answer[y][x]=num
    for _ in range(1, n):#←
        x-=1
        num+=1
        answer[y][x]=num
    for _ in range(1, n-1):#↑
        y-=1
        num+=1
        answer[y][x]=num
    return assign(y, x+1, num+1,n-2)