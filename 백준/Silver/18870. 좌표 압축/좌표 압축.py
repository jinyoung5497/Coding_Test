# 문제 분석
'''
- n개의 좌표를 압축한다
- Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
'''
# 의사 결정
'''
- 
'''
from sys import stdin

num = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
# 중복을 없애고 정렬한다
sorted_numbers = sorted(set(numbers))
# 딕셔너리에 좌표 값을 키로 인덱스를 벨류로 넣는다
dic = {sorted_numbers[i]: i for i in range(len(sorted_numbers))}

for i in numbers:
		# numbers에 값을 키로 넣어서 정렬된 딕셔너리에 값을 찾는다
    print(dic[i], end=" ")