def solution(my_string, indices):
    str = []
    for i in my_string:
        str.append(i)
    for i in indices:
        str[i] = ''
          
    return ''.join(str)

