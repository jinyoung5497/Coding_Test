def solution(s):
    stack = []
    flag = False
    for i in s:
        if i == "(":
            stack.append(i)
        elif stack and i == ")":
            stack.pop()
            flag = True
        if not stack and i == ")" and not flag:
            return False
    if stack or not flag:
        return False

    return True