def solution(id_list, report, k):
    set_report = set(report)
    reported = {}
    for i in set_report:
        a, b = i.split()
        if b in reported:
            reported[b] += 1
        else:
            reported[b] = 1

    count = {}
    for i in set_report:
        a, b = i.split()
        if a in count:
            if b in count[a]:
                break
            else:
                count[a].append(b)
        else:
            count[a] = [b]

    answer = []
    for i in id_list:
        cnt = 0
        if i in count:
            for j in count[i]:
                if reported[j] >= k:
                    cnt += 1
            answer.append(cnt)
        else:
            answer.append(0)
    return answer