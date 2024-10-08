from sys import stdin

n = int(stdin.readline())
numbers = []
common_num = {}

for _ in range(n):
    numbers.append(int(stdin.readline()))

if len(numbers) > 1:
    sum_numbers = sum(numbers) / n
    print(round(sum_numbers))
else:
    print(numbers[0])

sorted_numbers = sorted(numbers)
mid = len(sorted_numbers) // 2
print(sorted_numbers[mid])

for i in numbers:
    if i in common_num:
        common_num[i] += 1
    else:
        common_num[i] = 1

max_frequency = max(common_num.values())

frequencies = [i for i, freq in common_num.items() if freq == max_frequency]
frequencies.sort()

if len(frequencies) >= 2:
    print(frequencies[1])
else:
    print(frequencies[0])

print(max(numbers) - min(numbers))