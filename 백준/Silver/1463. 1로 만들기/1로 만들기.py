import sys
input = sys.stdin.readline

N = int(input().strip())

# DP 배열 초기화
dp = [0] * (N + 1)

for i in range(2, N + 1):
    # 기본적으로 -1을 한 경우
    dp[i] = dp[i - 1] + 1
    
    # 2로 나눌 수 있는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    # 3으로 나눌 수 있는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])