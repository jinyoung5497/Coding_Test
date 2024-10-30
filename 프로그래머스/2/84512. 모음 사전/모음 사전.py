from itertools import product


def solution(word):
    answer = []
    given_word = ["A", "E", "I", "O", "U"]

    # 각 길이에 맞는 모든 조합을 생성하고 answer에 추가
    for i in range(1, 6):
        for comb in product(given_word, repeat=i):
            answer.append(''.join(comb))

    # answer를 사전순으로 정렬
    sorted_list = sorted(answer)

    # word가 사전순으로 몇 번째인지 찾기
    return sorted_list.index(word) + 1