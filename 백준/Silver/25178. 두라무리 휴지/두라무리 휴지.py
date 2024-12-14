from sys import stdin
input = stdin.readline

n = int(input().strip())
word1 = input().strip()
word2 = input().strip()

# 첫 문자와 마지막 문자가 다르면 불가능
if word1[0] != word2[0] or word1[-1] != word2[-1]:
    print('NO')
    exit()

# 모음을 제거한 문자열 비교
def remove_vowels(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return ''.join(c for c in word if c not in vowels)

new_word1 = remove_vowels(word1)
new_word2 = remove_vowels(word2)

# 모음을 제거한 문자열이 다르면 불가능
if new_word1 != new_word2:
    print('NO')
    exit()

# 문자 빈도 비교
test_word1 = sorted(word1[1:-1])  # 슬라이싱 후 정렬
test_word2 = sorted(word2[1:-1])  # 슬라이싱 후 정렬

if test_word1 == test_word2:
    print('YES')
else:
    print('NO')
