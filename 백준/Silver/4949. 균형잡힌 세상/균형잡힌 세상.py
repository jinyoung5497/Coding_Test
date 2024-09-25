while True:
    str = input()
    stack = []
    if str == '.':
        break
    for i in str:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break

    if not len(stack):
        print("yes")
    else:
        print("no")
