# 입력받기 및 처리
input_list = map(int, input().split())

# 제곱의 합을 10으로 나눈 나머지 계산
ans_num = sum(i * i for i in input_list) % 10

# 결과 출력
print(ans_num)