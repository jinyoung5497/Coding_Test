from sys import stdin

input = stdin.readline

cs = []
for _ in range(20):
    cs.append(input().split())

grades = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

total_credit = 0
total_grade = 0
subject_grade= 0

for subject, credit, grade in cs:
    if grade == 'P':
        continue
    total_grade += grades[grade]
    total_credit += int(credit[0])
    subject_grade += grades[grade] * int(credit[0])
print(subject_grade / total_credit)