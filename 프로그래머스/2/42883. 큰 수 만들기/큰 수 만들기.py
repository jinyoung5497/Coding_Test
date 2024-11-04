def solution(number, k):
    answer = []
    count = 0
def solution(number, k):
    answer = []
    count = 0
    for i in number:
        if not answer:
            answer.append(i)
            continue
        if i < answer[-1]:
            answer.append(i)
        else:
            for j in range(len(answer) - 1, -1, -1):
                if answer[j] < i:
                    if count == k:
                        break
                    count += 1
                    answer.pop()
                else:
                    break
            answer.append(i)
    if count < k:
        leftCount = k - count
        for i in range(leftCount):
            answer.pop()
    return ''.join(answer)