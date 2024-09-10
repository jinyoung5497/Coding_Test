# 횟수 카운트 변수
count = 0

# 코드 1 재귀 함수 피보나치 시퀀스
def fib(n):
    if n == 1 or n == 2:
        return 1

    f = [0] * (n + 1)  # n + 1 개수 만큼의 list 숫자 확보 (f[0]은 0이라서 제외)
    f[1], f[2] = 1, 1  # f[1] = 1 f[2] = 1

    for i in range(3, n + 1):  # f[3] 부터 n번 만큼 값 입력
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

# 코드 2 동적 프로그래밍 피보나치 시퀀스
def fibonacci(n):
    global count # 실행 횟수 변수
    if n == 1 or n == 2:
        return 1

    f = [0] * (n + 1) # n + 1 개수 만큼의 list 숫자 확보 (f[0]은 0이라서 제외)
    f[1], f[2] = 1, 1 # f[1] = 1 f[2] = 1

    for i in range(3, n + 1): # f[3] 부터 n번 만큼 값 입력
        count += 1 # 실행 횟수 증가
        f[i] = f[i - 1] + f[i - 2]
    return count

num = int(input())
print(fib(num), fibonacci(num))