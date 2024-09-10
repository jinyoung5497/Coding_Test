# 입력 받기
input_data = input()

# 입력된 값을 공백을 기준으로 나누기
A, B = input_data.split()

# 문자열을 정수로 변환
A = int(A)
B = int(B)

# 비교 결과 출력
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")