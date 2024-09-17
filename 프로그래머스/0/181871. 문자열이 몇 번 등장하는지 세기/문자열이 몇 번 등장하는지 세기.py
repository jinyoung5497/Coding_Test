def solution(myString, pat):
    answer = 0
    for i, c in enumerate(myString):
        if myString[i:i + len(pat)] == pat:
            answer += 1
                
    return answer