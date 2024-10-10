def solution(progresses, speeds):
    answer = []
    number = {}

    for i in range(len(progresses)):
        count = 0
        while progresses[i] < 100:
            count += 1
            progresses[i] += speeds[i]
        answer.append(count)
    for i in range(len(answer) - 1):
        if answer[i] > answer[i + 1]:
            answer[i + 1] = answer[i]
    for i in answer:
        if i in number:
            number[i] += 1
        else:
            number[i] = 1

    return list(number.values())