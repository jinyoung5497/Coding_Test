def solution(myString, pat):
    index = myString.rfind(pat)
    if index != -1:
        return myString[:index + len(pat)]
    return myString