def solution(num_list):
       
    odd = []
    even = []
    for i in num_list:
        if i % 2 == 1:
            odd.append(i)
        else: even.append(i)
    odd = ''.join(map(str, odd))
    even = ''.join(map(str, even))
    answer = int(odd) + int(even)
    return answer