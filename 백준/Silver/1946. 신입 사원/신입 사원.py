from sys import stdin

num = int(stdin.readline())

for _ in range(num):
    score = []
    answer = 1
    case = int(stdin.readline())
    for _ in range(case):
        a, b = list(map(int, stdin.readline().split()))
        score.append((a, b))

    sorted_score = sorted(score, key=lambda x: x[0])
    new_a, new_b = sorted_score[0]
    for i in range(1, len(sorted_score)):
        comp_a, comp_b = sorted_score[i]
        if new_b > comp_b:
            answer += 1
            new_b = sorted_score[i][1]
    print(answer)