num_students = int(input())
pick_num = list(map(int, input().split()))
student_list = []

for i in range(num_students):
    student_list.insert(pick_num[i], i + 1)

print(*student_list[::-1])