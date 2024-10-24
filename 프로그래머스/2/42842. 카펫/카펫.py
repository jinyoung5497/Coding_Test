def solution(brown, yellow):
    factor = []
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            factor.append([i, yellow // i])

    for a, b in factor:
        answer = 0
        horizontal = (b + 2)
        vertical = a
        answer += horizontal * 2 + vertical * 2
        if answer == brown:
            return [horizontal, vertical + 2]