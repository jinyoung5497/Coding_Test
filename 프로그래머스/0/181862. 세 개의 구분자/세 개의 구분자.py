def solution(myStr):
    answer = myStr.replace("a", ' ').replace("b", ' ').replace("c", ' ').strip().split()
    if not answer:
        answer = ["EMPTY"]
    return answer