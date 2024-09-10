input_num = int(input())
string_list = [input() for _ in range(input_num)]
count = 0
def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global count
    count = 0
    return recursion(s, 0, len(s)-1)

for i in string_list:
    print(isPalindrome(i), count)