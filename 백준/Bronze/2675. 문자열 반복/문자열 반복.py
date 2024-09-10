# 인풋 입력
input_num = int(input())
input_list = []

for _ in range(input_num):
    num, text = input().split()
    input_list.append((int(num), text))

# 문자열 반복
for i in input_list:
    num = i[0]
    text = i[1]
    for char in text:
        print(char * num, end='')
    print()