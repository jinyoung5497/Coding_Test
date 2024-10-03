from sys import stdin

num = int(stdin.readline())
words = sorted(set(stdin.readline().strip() for _ in range(num)))
sorted_words = sorted(words, key=lambda x: len(x))

for i in sorted_words:
    print(i)