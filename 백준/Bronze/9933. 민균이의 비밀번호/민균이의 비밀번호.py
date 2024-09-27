# 백준 얘는 참 말을 잘 못하는거 같다
num = int(input())
words = [input() for _ in range(num)]
length = 0
middle = 0
for i in words:
    if i[::-1] in words:
        length = len(i)
        middle = i[length // 2]
        break
print(length, middle)



