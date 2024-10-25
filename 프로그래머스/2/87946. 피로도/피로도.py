from itertools import permutations
def solution(k, dungeons):
    answer = []
    permutation = list(permutations(dungeons))
    for i in permutation:
        count = 0
        my_health = k
        for j in range(len(i)):
            min_health = i[j][0]
            used_health = i[j][1]
            if my_health >= min_health:
                my_health -= used_health
                count += 1
            else:
                break
        answer.append(count)

    return max(answer)