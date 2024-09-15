def solution(num_list):
    answer = 0
    odd = 0
    even = 0
    for i,n in enumerate(num_list):
        if i % 2 == 0:
            even += n
        else:
            odd += n
    if odd > even:
        answer = odd
    else: answer = even
    return answer