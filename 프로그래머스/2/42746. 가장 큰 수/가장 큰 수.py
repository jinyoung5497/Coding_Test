def solution(numbers):
    answer = ''
    new_num = list(map(str, numbers))
    sorted_numbers = sorted(new_num, key=lambda x: x*3, reverse=True)
    sorted_numbers = str(int(''.join(sorted_numbers)))

    return sorted_numbers