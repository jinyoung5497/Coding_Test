def solution(todo_list, finished):
    answer = []
    for i, n in enumerate(finished):
        if not n:
            answer.append(todo_list[i])
    return answer